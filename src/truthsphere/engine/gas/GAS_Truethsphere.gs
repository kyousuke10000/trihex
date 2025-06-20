/**
 * 💎 Inner Quest Book 自動書き込み Webhook（統一列版）
 *   - すべての Week シート G〜L 列のヘッダーを
 *     「意味 / 価値観・信念 / 現在への影響 / 誇り / 再統合メッセージ / 未完了テーマ」
 *     で統一していることが前提
 *   - JSON 例は本文の後ろに記載
 */

// ==== 設定項目 ==============================================================
const TOKEN_EXPECTED = 'soulflow2025';        // Webhook 共有トークン
const START_COL      = 7;                     // G 列 = 7
const COLUMN_LIST    = [                      // G〜L に並ぶ 6 項目
  '意味', '価値観・信念', '現在への影響',
  '誇り', '再統合メッセージ', '未完了テーマ'
];
// =============================================================================

/**
 * Cloudflare Worker / GPT Action からの POST を処理
 * @param {GoogleAppsScript.Events.DoPost} e
 * @returns {ContentService.Output}
 */
function doPost(e) {
  // --- 生データ取得 ---------------------------------------------------------
  const raw = e?.postData?.contents;
  if (!raw) return txt('Missing postData');

  let body;
  try {
    body = JSON.parse(raw);
  } catch (err) {
    return txt('Invalid JSON');
  }

  // GPT Action 形式 (parameters フィールド) / 手動 JSON の両方に対応
  const p = body.parameters || body;

  // --- トークン検証 ---------------------------------------------------------
  if (p.token !== TOKEN_EXPECTED) return txt('Unauthorized');

  // --- 必須パラメータ取得 ---------------------------------------------------
  const row  = parseInt(p.row, 10);
  const week = (p.week || '').trim();  // 前後空白除去

  if (!row || !week) return txt('Missing row or week');

  // --- 対象シート取得 -------------------------------------------------------
  const ss    = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName(week);
  if (!sheet) return txt('Sheet not found: ' + week);

  // --- 書き込む値を G〜L 列分組み立て --------------------------------------
  const values = COLUMN_LIST.map(k => (p[k] ?? '').toString());

  // --- 実行ログ（デバッグ用） ----------------------------------------------
  console.log(`▶ ${week} row=${row} → ${JSON.stringify(values)}`);

  // --- 書き込み -------------------------------------------------------------
  sheet.getRange(row, START_COL, 1, values.length).setValues([values]);

  return txt('OK');
}

/* -------------------------------------------------------------------------- */
/* ヘルパー関数                                                               */
/* -------------------------------------------------------------------------- */
function txt(s) {
  return ContentService.createTextOutput(s);
}

/* -------------------------------------------------------------------------- */
/* 手動テスト用ダミー関数（IDE で試したいときだけ実行）                       */
/* -------------------------------------------------------------------------- */
function testLocal() {
  const mock = {
    token: TOKEN_EXPECTED,
    week : 'Week4_世界観',
    row  : 3,
    意味         : '理不尽を超えた先の光',
    '価値観・信念' : '努力は報われる',
    現在への影響   : '不条理を見ると行動せずにいられない',
    誇り           : '闇の中でも灯を掲げる勇気',
    再統合メッセージ : 'その灯を分け与えよ',
    未完了テーマ     : ''
  };
  // doPost と同じ関数を直接呼び出し
  doPost({ postData: { contents: JSON.stringify(mock) } });
}
