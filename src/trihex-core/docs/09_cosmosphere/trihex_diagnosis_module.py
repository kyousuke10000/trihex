# 6R:Fire
from datetime import date

import ephem
from life_path_utils import calculate_life_path  # 数秘モジュールの正規統合

# 正確な干支マスタ辞書（例：1980〜2040年）
eto_year_dict = {
    1980: "庚申",
    1981: "辛酉",
    1982: "壬戌",
    1983: "癸亥",
    1984: "甲子",
    1985: "乙丑",
    1986: "丙寅",
    1987: "丁卯",
    1988: "戊辰",
    1989: "己巳",
    1990: "庚午",
    1991: "辛未",
    1992: "壬申",
    1993: "癸酉",
    1994: "甲戌",
    1995: "乙亥",
    1996: "丙子",
    1997: "丁丑",
    1998: "戊寅",
    1999: "己卯",
    2000: "庚辰",
    2001: "辛巳",
    2002: "壬午",
    2003: "癸未",
    2004: "甲申",
    2005: "乙酉",
    2006: "丙戌",
    2007: "丁亥",
    2008: "戊子",
    2009: "己丑",
    2010: "庚寅",
    2011: "辛卯",
    2012: "壬辰",
    2013: "癸巳",
    2014: "甲午",
    2015: "乙未",
    2016: "丙申",
    2017: "丁酉",
    2018: "戊戌",
    2019: "己亥",
    2020: "庚子",
    2021: "辛丑",
    2022: "壬寅",
    2023: "癸卯",
    2024: "甲辰",
    2025: "乙巳",
    2026: "丙午",
    2027: "丁未",
    2028: "戊申",
    2029: "己酉",
    2030: "庚戌",
    2031: "辛亥",
    2032: "壬子",
    2033: "癸丑",
    2034: "甲寅",
    2035: "乙卯",
    2036: "丙辰",
    2037: "丁巳",
    2038: "戊午",
    2039: "己未",
    2040: "庚申",
}


def get_eto_from_date(year: int, month: int, day: int) -> str:
    """
    年月日から正確な干支を取得（立春基準での年切替含む）
    """
    date_str = f"{year}/{month}/{day}"
    target_date = date(year, month, day)

    # 毎年1月20日を起点に「立春」（315度通過点）を計算
    solar_term = ephem.next_crossing(
        ephem.Sun(315 * ephem.degree), ephem.Date(f"{year}/1/20")
    )
    start_of_spring = solar_term.datetime().date()

    # 干支年を立春判定に基づいて調整
    eto_year = year if target_date >= start_of_spring else year - 1

    # 正確な干支を辞書から取得
    eto = eto_year_dict.get(eto_year, "不明")
    return eto


def get_life_path_number(year: int, month: int, day: int) -> int:
    """
    正規ライフパスナンバーを取得する（補助数秘は扱わない）
    """
    return calculate_life_path(year, month, day)


# テスト実行
if __name__ == "__main__":
    print("干支:", get_eto_from_date(1981, 3, 24))  # 結果：辛酉
    print("数秘:", get_life_path_number(1981, 3, 24))  # 結果：1
