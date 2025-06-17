# トライヘックス 🔥 / Trihex

**Trihex** は占い系マイクロサービス・データユーティリティ・Web フロントエンドを
ひとまとめに管理する *モノレポ* です。

> すべてのソースコード冒頭には `# 6R:Fire` もしくは `//6R:Fire` を付与し、
> “再点火版（Re‑ignited Edition）” であることを示しています。

---

## 目次

1. [概要](#概要)
2. [クイックスタート](#クイックスタート)
3. [ディレクトリ構成](#ディレクトリ構成)
4. [開発フロー](#開発フロー)
5. [テスト](#テスト)
6. [貢献方法](#貢献方法)
7. [ライセンス](#ライセンス)
8. [English Summary](#english-summary)

---

## 概要
| ディレクトリ | 役割 |
| `src/`   | 本番コード（Flask Webhook、Streamlit UI など） |
| `tests/` | Pytest スモークテスト（インポート確認） |
| `assets/`| 画像・ロゴ |
| `docs/`  | 設計資料・ADR |
| `data/`  | 固定データ |
| `.claude/` | Claude Code の作業ログ |


---

## クイックスタート

```bash
# クローン
git clone git@github.com:kyousuke10000/trihex.git
cd trihex

# 仮想環境
python3 -m venv .venv
source .venv/bin/activate

# 依存インストール（Streamlit は少し時間がかかります）
pip install -r src/trihex_gpt_custom/requirements.txt

# Streamlit フロントエンド起動
streamlit run src/trihex_gpt_custom/app.py

# Flask Webhook 起動（ローカル検証用）
python src/soul-diagnosis-webhook/app.py
```

> ※ もともと個別 Git リポジトリだったサブフォルダもあります。
> 必要に応じてサブモジュール化してください。

---

## ディレクトリ構成

```text
trihex
├─ assets/
├─ data/
├─ docs/
├─ src/
│  ├─ soul-diagnosis-webhook/   # Flask
│  ├─ trihex_gpt_custom/        # Streamlit
│  ├─ trihex-core/              # コアロジック
│  └─ trihex-infra/             # Cloudflare / GAS プロキシ
├─ tests/
├─ .gitignore
└─ README.md
```

---

## 開発フロー

1. ブランチ作成
   `git checkout -b feat/<トピック>`
2. コーディング → コミット（ファイル冒頭に `6R:Fire` 追加を忘れずに）
3. テスト実行 `pytest -q`
4. プッシュして PR 作成（将来的に GitHub Actions で自動テスト予定）

---

## テスト

* `tests/test_imports.py` によるスモークテストで **import エラー** を検出
* 追加テストは `tests/<module>/test_*.py` で管理してください

```bash
pip install pytest
pytest -q
```

---

## 貢献方法

1. Fork → Branch → PR
2. コミットメッセージは `feat:` / `fix:` など Conventional Commits 風
3. `pre-commit` 導入予定

バグ報告・機能提案・ドキュメント改善など大歓迎です！

---

## ライセンス

MIT License – 詳細は [`LICENSE`](LICENSE) を参照してください。

---

## English Summary

Trihex is a **monorepo** containing the webhook, Streamlit UI, core diagnosis engine and Cloudflare proxies for the Trihex project.

See the English comments inside each section if you’d like to contribute!

---

*Made with ❤️  & `# 6R:Fire`.*
