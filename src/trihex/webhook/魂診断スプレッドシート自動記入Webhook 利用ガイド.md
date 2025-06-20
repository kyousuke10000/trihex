# 魂診断スプレッドシート自動記入Webhook 利用ガイド

## 概要
このWebhookは、外部からPOSTされたデータを元に、指定されたGoogleスプレッドシートの特定シートと行に魂診断の結晶項目を自動記入するためのものです。

## セットアップ手順

### 1. Googleサービスアカウントの準備
1. [Google Cloud Platform](https://console.cloud.google.com/)にアクセスし、新しいプロジェクトを作成します
2. Google Sheets APIとGoogle Drive APIを有効にします
3. サービスアカウントを作成し、認証情報（JSONファイル）をダウンロードします
4. ダウンロードしたJSONファイルを`credentials.json`としてWebhookサーバーに配置します
5. 対象のGoogleスプレッドシートをサービスアカウントのメールアドレスと共有します（編集権限が必要）

### 2. 環境変数の設定
以下の環境変数を設定します：
- `GOOGLE_APPLICATION_CREDENTIALS`: 認証情報JSONファイルのパス（例: `credentials.json`）
- `SPREADSHEET_ID`: 対象のGoogleスプレッドシートのID
- `PORT`: Webhookサーバーのポート番号（デフォルト: 5000）

### 3. Webhookサーバーの起動
```bash
# 必要なライブラリのインストール
pip install flask gspread oauth2client

# サーバー起動
./run.sh
```

または、直接Pythonで実行：
```bash
export GOOGLE_APPLICATION_CREDENTIALS="credentials.json"
export SPREADSHEET_ID="your_spreadsheet_id_here"
export PORT=5000
python app.py
```

## APIエンドポイント
- ローカル開発環境: `http://localhost:5000/webhook/soul-diagnosis`
- 本番環境: `https://your-domain.com/webhook/soul-diagnosis`

## リクエスト例
以下のようなJSONデータをPOSTします：

```json
{
  "week": "Week1_自分史",
  "row": 3,
  "意味": "過去の困難な経験から学んだ強さ",
  "価値観・信念": "困難があっても諦めない粘り強さが大切",
  "現在への影響": "困難な状況でも冷静に対処できる自信がある",
  "誇り": "どんな状況でも前向きに取り組める姿勢",
  "再統合メッセージ": "あなたの経験は無駄ではなく、今のあなたを形作る大切な要素です",
  "未完了テーマ": "自分の弱さも受け入れること"
}
```

## curlでのテスト方法
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d @sample_request.json \
  http://localhost:5000/webhook/soul-diagnosis
```

## レスポンス例
### 成功時
```json
{
  "status": "success",
  "message": "データを正常に書き込みました",
  "details": {
    "sheet": "Week1_自分史",
    "row": 3,
    "columns_updated": ["意味", "価値観・信念", "現在への影響", "誇り", "再統合メッセージ", "未完了テーマ"]
  }
}
```

### エラー時
```json
{
  "status": "error",
  "message": "エラーメッセージ",
  "error_code": "ERROR_CODE"
}
```

## ログの確認
操作ログは `webhook.log` ファイルに記録されます。エラーや成功の詳細を確認できます。

## 注意事項
- 既存のセル内容は上書きされます
- 送信されなかった項目は更新されません（空欄にはなりません）
- 「最後の気づき（自由記述）」はPOSTで送られてきた場合のみ記入されます
- スプレッドシートのヘッダー行（1行目）には、記入項目と完全一致する列名が必要です
