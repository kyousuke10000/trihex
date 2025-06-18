# 6R:Fire


def trihex_diagnose(eto: str, life_path: int, now_kanji: str, ideal_kanji: str):
    if eto == "壬子" and life_path == 11:
        spiral = "識"
    else:
        spiral = {
            "木_陽": "風",
            "木_陰": "空",
            "火_陽": "火",
            "火_陰": "火",
            "土_陽": "地",
            "土_陰": "地",
            "金_陽": "風",
            "金_陰": "風",
            "水_陽": "水",
            "水_陰": "水",
        }.get(
            f"{eto_dict.get(eto, {{}}).get('五行')}_{eto_dict.get(eto, {{}}).get('陰陽')}",
            "不明",
        )
    system = {
        "義": "智略",
        "和": "共鳴",
        "動": "行動",
        "創": "創造",
        "空": "直感",
        "信": "信念",
    }.get(now_kanji, "不明")
    wisdom = {
        "構": "數理",
        "共": "陰陽",
        "変": "易変",
        "螺": "螺律",
        "夢": "霊脈",
        "形": "真形",
    }.get(ideal_kanji, "不明")
    return {
        "干支": eto,
        "数秘": life_path,
        "今の漢字": now_kanji,
        "理想の漢字": ideal_kanji,
        "先天螺旋": spiral,
        "後天系統": system,
        "顕現叡智": wisdom,
    }
