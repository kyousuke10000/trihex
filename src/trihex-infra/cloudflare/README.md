# ☁️ Cloudflare Workers 中継一覧

このディレクトリは、TriHexプロジェクトにおける各種サービスとの接続を中継する **Cloudflare Worker群** を管理しています。

## 📦 構成

| ディレクトリ | 中継元 → 中継先 | 説明 |
|--------------|------------------|------|
| `flask_proxy/` | AI／GAS → Flask（Render） | 魂診断の内容をRenderのFlaskサーバーに転送し、Slack通知やPDF化処理をトリガーします |
| `gas_proxy/` | AI／GPT → GAS | 魂診断の回答内容をGoogle Sheetsに記入するため、GASスクリプトに転送します |
| `discord_proxy/` | 🔜 今後追加予定 | Discord連携を想定したWorkerの配置場所です |
| `notion_proxy/` | 🔜 今後追加予定 | Notionとの中継用コードを配置予定です |

---

## 🛠️ 各Workerの中身

### 🔁 `flask_proxy/`
- `Cloudflare_to_Flask.js`：Flask（Render）への中継コード
- `wrangler.toml`：Cloudflare用設定
- `sample_request_flask.json`：POST例
- [`README.md`](./flask_proxy/README.md)

### 🔁 `gas_proxy/`
- `Cloudflare_to_GAS.js`：GAS中継コード
- `sample_request_gas.json`：POST例
- [`README.md`](./gas_proxy/README.md)

---

## 🧩 使い方概要

1. Cloudflare Workerで中継コードをホスト
2. 外部のAI／ツールからCloudflareのURLにPOST
3. WorkerがFlask／GASにリクエストをそのまま転送
4. 各サービスでSlack通知／スプレッドシート書き込みなどを実行

---

## 🔮 拡張予定

- `discord_proxy/`：魂診断結果のDiscord連携
- `notion_proxy/`：Notion DBへの記録
- `line_proxy/`：LINEへの連携機構（構想中）

---

## 🧠 制作背景

- Cloudflareを使う理由：**セキュリティとAPI連携の柔軟性確保**
- GPT／外部サービスが **RenderやGASのURLを直接叩かずに済む**設計で、保守性・安全性が高まります。

---

## ✍️ 編集メモ（開発用）

- 全てのWorkerは `/webhook/soul-diagnosis` 等、**固定パスで設計**
- wrangler.toml を使えばCLIデプロイも可能
