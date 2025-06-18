# 🌐 Cloudflare → Flask 中継Worker

このフォルダは、魂診断の結果を Flask Webhook（Render）に中継するCloudflare Workerを管理しています。

## 使用ファイル

- `Cloudflare_to_Flask.js`：中継コード本体
- `wrangler.toml`：Cloudflare CLI設定
- `sample_request_flask.json`：POSTテスト用データ

## 中継先

`https://soul-diagnosis-webhook.onrender.com/webhook/soul-diagnosis`
