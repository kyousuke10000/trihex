# 6R:Fire
from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
import logging
from datetime import datetime
import requests  # Slack通知のために追加

# ---------------------------
# ロギング設定
# ---------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('webhook.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('soul-diagnosis-webhook')

app = Flask(__name__)

# ---------------------------
# 魂診断のスプレッド書き込み対象項目
# ---------------------------
SOUL_DIAGNOSIS_COLUMNS = [
    "意味", "価値観・信念", "現在への影響", "誇り", "再統合メッセージ",
    "未完了テーマ", "最後の気づき（自由記述）"
]

# ---------------------------
# Google Sheetsクライアントの取得
# ---------------------------
def get_spreadsheet_client():
    try:
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds_file = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', 'credentials.json')
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
        client = gspread.authorize(creds)

        spreadsheet_id = os.environ.get('SPREADSHEET_ID')
        if not spreadsheet_id:
            logger.error("SPREADSHEET_ID環境変数が設定されていません")
            return None

        spreadsheet = client.open_by_key(spreadsheet_id)
        return spreadsheet
    except Exception as e:
        logger.error(f"スプレッドシートクライアントの初期化エラー: {str(e)}")
        return None

# ---------------------------
# Webhook 1：スプレッドシート自動記入
# ---------------------------
@app.route('/webhook/soul-diagnosis', methods=['POST'])
def soul_diagnosis_webhook():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"status": "error", "message": "JSONデータが見つかりません", "error_code": "INVALID_REQUEST"}), 400

        if 'week' not in data or 'row' not in data:
            return jsonify({"status": "error", "message": "必須パラメータ(week, row)が不足しています", "error_code": "MISSING_REQUIRED_PARAMS"}), 400

        sheet_name = data['week']
        try:
            row = int(data['row'])
        except ValueError:
            return jsonify({"status": "error", "message": "行番号は整数である必要があります", "error_code": "INVALID_REQUEST"}), 400

        spreadsheet = get_spreadsheet_client()
        if not spreadsheet:
            return jsonify({"status": "error", "message": "スプレッドシートへの接続に失敗しました", "error_code": "AUTH_ERROR"}), 500

        try:
            worksheet = spreadsheet.worksheet(sheet_name)
        except gspread.exceptions.WorksheetNotFound:
            return jsonify({"status": "error", "message": f"シート '{sheet_name}' が見つかりません", "error_code": "SHEET_NOT_FOUND"}), 404

        updated_columns = []
        for column in SOUL_DIAGNOSIS_COLUMNS:
            if column in data and data[column]:
                try:
                    header_row = worksheet.row_values(1)
                    if column not in header_row:
                        logger.warning(f"列 '{column}' がシート内に見つかりません")
                        continue
                    col_idx = header_row.index(column) + 1
                    worksheet.update_cell(row, col_idx, data[column])
                    updated_columns.append(column)
                    logger.info(f"セル更新: シート={sheet_name}, 行={row}, 列={column}, 値={data[column][:20]}...")
                except Exception as e:
                    logger.error(f"セル更新エラー: {str(e)}")
                    return jsonify({"status": "error", "message": f"セル更新中にエラーが発生しました: {str(e)}", "error_code": "SPREADSHEET_ERROR"}), 500

        return jsonify({
            "status": "success",
            "message": "データを正常に書き込みました",
            "details": {
                "sheet": sheet_name,
                "row": row,
                "columns_updated": updated_columns
            }
        }), 200

    except Exception as e:
        logger.error(f"Webhookエラー: {str(e)}")
        return jsonify({"status": "error", "message": f"内部サーバーエラー: {str(e)}", "error_code": "INTERNAL_ERROR"}), 500

# ---------------------------
# Webhook 2：Slack通知
# ---------------------------
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

@app.route("/api/receive_soul_diagnosis", methods=["POST"])
def receive_soul_diagnosis():
    data = request.json
    soul_no = data.get("soul_no")
    soul_name = data.get("soul_name")
    pdf_url = data.get("pdf_url")

    message = f"""
🧭 魂診断結果のお知らせ

魂No: {soul_no}
魂名: {soul_name}
📄 PDF URL: {pdf_url}
"""

    slack_response = requests.post(
        SLACK_WEBHOOK_URL,
        data=json.dumps({"text": message}),
        headers={"Content-Type": "application/json"}
    )

    if slack_response.status_code != 200:
        return jsonify({"status": "error", "message": slack_response.text}), 500

    return jsonify({"status": "success", "message": "Slack通知完了"}), 200

# ---------------------------
# Flask起動設定
# ---------------------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
