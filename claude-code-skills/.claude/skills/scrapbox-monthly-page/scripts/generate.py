#!/usr/bin/env python3
"""
Scrapbox月次ページ生成スクリプト
指定した年月のScrapbox形式の月次ページを生成する
"""

import sys
import calendar
from datetime import date


def get_japanese_weekday(weekday: int) -> str:
    """曜日番号（0=月曜）を日本語1文字に変換"""
    weekdays = ["月", "火", "水", "木", "金", "土", "日"]
    return weekdays[weekday]


def get_prev_month(year: int, month: int) -> tuple[int, int]:
    """前月の年月を取得"""
    if month == 1:
        return year - 1, 12
    return year, month - 1


def get_next_month(year: int, month: int) -> tuple[int, int]:
    """翌月の年月を取得"""
    if month == 12:
        return year + 1, 1
    return year, month + 1


def generate_monthly_page(year: int, month: int) -> str:
    """月次ページを生成"""
    lines = []

    # タイトル
    lines.append(f"{year}/{month:02d}")

    # ナビゲーション
    prev_year, prev_month = get_prev_month(year, month)
    next_year, next_month = get_next_month(year, month)
    lines.append(f"[{prev_year}/{prev_month:02d}] ← →[{next_year}/{next_month:02d}]")
    lines.append("")

    # 日付リスト
    _, days_in_month = calendar.monthrange(year, month)
    for day in range(1, days_in_month + 1):
        d = date(year, month, day)
        weekday = get_japanese_weekday(d.weekday())
        lines.append(f"[{year}/{month:02d}/{day:02d}]({weekday}) ")

    return "\n".join(lines)


def main():
    if len(sys.argv) != 2:
        print("Usage: python generate.py YYYY-MM")
        print("Example: python generate.py 2025-11")
        sys.exit(1)

    try:
        year_month = sys.argv[1]
        year, month = map(int, year_month.split("-"))
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12")
    except ValueError as e:
        print(f"Error: Invalid date format. Use YYYY-MM (e.g., 2025-11)")
        print(f"Details: {e}")
        sys.exit(1)

    result = generate_monthly_page(year, month)
    print(result)


if __name__ == "__main__":
    main()
