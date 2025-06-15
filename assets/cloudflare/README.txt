▼ このパックの使い方：

1. `openapi.yaml` をカスタムGPTの Actions スキーマに読み込む。
   - サーバーURLは Cloudflare Workers のURLを指定済み。
   - トークン項目を含み、セキュリティも対応済み。

2. `postman_sample.json` をPostmanに貼り付け、POST送信してテスト可能。
   - URL: https://wispy-shape-5e10.kyousuke10000.workers.dev/
   - Headers: Content-Type: application/json

3. GPTの出力フォーマットがこのJSONと一致するようにプロンプトを設計。
   - token, row, weekは必須。
   - weekごとに項目は異なってOK（GAS側で柔軟に対応可能にすることが前提）

by Truthsphere連携チーム
