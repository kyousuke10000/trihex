# 📘 Truthsphere Quartz Model Documentation

このフォルダは、魂診断の12週モデルに基づいて、各週ごとの質問・要約・哲学を記録するためのドキュメント群です。

---

## 📁 フォルダ構造

docs/
└── quartz_model/
    ├── week1/
    │   ├── question_list.json
    │   └── quartz_summary.md
    └── week2/
        ├── question_list.json
        └── quartz_summary.md


---

## 🧠 設計意図（Quartz Philosophy）

- 本プロジェクトは、魂の深層を問う「Quartz Model（魂の結晶構造）」に基づいて構築されています。
- 各 `question_list.json` はその週における魂の深層問い（Core Inquiry）を定義します。
- 各 `quartz_summary.md` は Truthsphere（スフィ）との対話により生まれた魂の洞察を記録します。

---

## ✅ データフォーマット（JSON）

各質問は以下のフォーマットで構成されます：

```json
{
  "id": "Q1",
  "week": "Week2",
  "category": "快の直感",
  "text": "あなたが自然と心がぬくもり・テンションが上がるのはどんな場面？",
  "type": "question"
}
