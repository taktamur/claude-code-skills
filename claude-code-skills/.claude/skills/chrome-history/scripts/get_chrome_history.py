#!/usr/bin/env python3
"""
Chrome履歴取得スクリプト
全項目を取得し、複数のフォーマットで出力可能
"""

import sqlite3
import shutil
import argparse
import json
import csv
import os
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
from collections import Counter
import sys

# Chromeの履歴データベースのパス（macOS）
CHROME_HISTORY_PATH = os.path.expanduser(
    "~/Library/Application Support/Google/Chrome/Default/History"
)

# Chromeのタイムスタンプを変換（Chrome epoch: 1601-01-01）
def chrome_timestamp_to_datetime(chrome_timestamp):
    """ChromeのタイムスタンプをPythonのdatetimeに変換"""
    if chrome_timestamp is None or chrome_timestamp == 0:
        return None
    # Chromeのエポックは1601-01-01、Unixエポックは1970-01-01
    # 差分: 11644473600秒
    unix_timestamp = chrome_timestamp / 1000000 - 11644473600
    try:
        return datetime.fromtimestamp(unix_timestamp)
    except (ValueError, OSError):
        return None

def get_transition_type_name(transition):
    """遷移タイプの数値を名前に変換"""
    types = {
        0: "LINK",
        1: "TYPED",
        2: "AUTO_BOOKMARK",
        3: "AUTO_SUBFRAME",
        4: "MANUAL_SUBFRAME",
        5: "GENERATED",
        6: "START_PAGE",
        7: "FORM_SUBMIT",
        8: "RELOAD",
        9: "KEYWORD",
        10: "KEYWORD_GENERATED",
    }
    # 下位8ビットがコアタイプ
    core_type = transition & 0xFF
    return types.get(core_type, f"UNKNOWN({core_type})")

def extract_domain(url):
    """URLからドメインを抽出"""
    try:
        parsed = urlparse(url)
        return parsed.netloc or parsed.path.split('/')[0]
    except:
        return ""

def get_chrome_history(limit=None, days=None):
    """
    Chrome履歴を取得

    Args:
        limit: 取得する件数の上限
        days: 過去何日分を取得するか

    Returns:
        list: 履歴データのリスト
    """
    # 履歴ファイルをコピー（Chromeが実行中はロックされているため）
    temp_db = "/tmp/chrome_history_copy.db"

    try:
        shutil.copy2(CHROME_HISTORY_PATH, temp_db)
    except FileNotFoundError:
        print(f"Error: Chrome履歴ファイルが見つかりません: {CHROME_HISTORY_PATH}", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Chrome履歴ファイルへのアクセス権限がありません", file=sys.stderr)
        sys.exit(1)

    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()

    # 全項目を取得するクエリ（urls + visits テーブルを結合）
    query = """
    SELECT
        urls.id,
        urls.url,
        urls.title,
        urls.visit_count,
        urls.typed_count,
        urls.last_visit_time,
        urls.hidden,
        visits.visit_time,
        visits.visit_duration,
        visits.transition,
        visits.from_visit
    FROM urls
    LEFT JOIN visits ON urls.id = visits.url
    """

    conditions = []
    params = []

    if days:
        # 過去N日分のフィルター
        current_time = datetime.now()
        chrome_time = (current_time.timestamp() + 11644473600) * 1000000
        days_ago = chrome_time - (days * 24 * 60 * 60 * 1000000)
        conditions.append("visits.visit_time > ?")
        params.append(days_ago)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " ORDER BY visits.visit_time DESC"

    if limit:
        query += f" LIMIT {limit}"

    cursor.execute(query, params)

    history = []
    for row in cursor.fetchall():
        visit_time = chrome_timestamp_to_datetime(row[7])
        last_visit_time = chrome_timestamp_to_datetime(row[5])

        history.append({
            'id': row[0],
            'url': row[1],
            'title': row[2],
            'visit_count': row[3],
            'typed_count': row[4],
            'last_visit_time': last_visit_time.isoformat() if last_visit_time else None,
            'hidden': bool(row[6]),
            'visit_time': visit_time.isoformat() if visit_time else None,
            'visit_duration': row[8],  # マイクロ秒
            'visit_duration_seconds': row[8] / 1000000 if row[8] else None,
            'transition_type': get_transition_type_name(row[9]) if row[9] is not None else None,
            'transition_raw': row[9],
            'from_visit': row[10],
            'domain': extract_domain(row[1])
        })

    conn.close()
    return history

def get_statistics(history):
    """履歴データから統計情報を生成"""
    domains = [h['domain'] for h in history if h['domain']]
    urls = [h['url'] for h in history]

    domain_counter = Counter(domains)
    url_counter = Counter(urls)

    # 時間帯の分析
    hours = []
    for h in history:
        if h['visit_time']:
            dt = datetime.fromisoformat(h['visit_time'])
            hours.append(dt.hour)

    hour_counter = Counter(hours)

    stats = {
        'total_records': len(history),
        'unique_urls': len(set(urls)),
        'unique_domains': len(set(domains)),
        'top_domains': domain_counter.most_common(10),
        'top_urls': url_counter.most_common(10),
        'visits_by_hour': dict(sorted(hour_counter.items())),
    }

    return stats

def export_csv(history, output_file):
    """CSV形式で出力"""
    if not history:
        print("履歴データがありません", file=sys.stderr)
        return

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=history[0].keys())
        writer.writeheader()
        writer.writerows(history)

    print(f"✅ CSV出力: {output_file}")

def export_tsv(history, output_file):
    """TSV形式で出力"""
    if not history:
        print("履歴データがありません", file=sys.stderr)
        return

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=history[0].keys(), delimiter='\t')
        writer.writeheader()
        writer.writerows(history)

    print(f"✅ TSV出力: {output_file}")

def export_json(history, output_file, stats=None):
    """JSON形式で出力"""
    data = {
        'history': history,
    }

    if stats:
        data['statistics'] = stats

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ JSON出力: {output_file}")

def export_markdown(history, output_file, stats=None):
    """Markdown形式で出力"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Chrome閲覧履歴\n\n")

        if stats:
            f.write("## 統計情報\n\n")
            f.write(f"- 総レコード数: {stats['total_records']}\n")
            f.write(f"- ユニークURL数: {stats['unique_urls']}\n")
            f.write(f"- ユニークドメイン数: {stats['unique_domains']}\n\n")

            f.write("### よく訪問するドメイン (Top 10)\n\n")
            for domain, count in stats['top_domains']:
                f.write(f"- {domain}: {count}回\n")
            f.write("\n")

            f.write("### 時間帯別訪問数\n\n")
            for hour, count in stats['visits_by_hour'].items():
                f.write(f"- {hour:02d}:00 - {count}回\n")
            f.write("\n")

        f.write("## 履歴一覧\n\n")
        f.write("| 訪問日時 | タイトル | URL | 訪問回数 | ドメイン |\n")
        f.write("|---------|---------|-----|----------|----------|\n")

        for h in history[:100]:  # 最初の100件のみ表示
            visit_time = h['visit_time'] or 'N/A'
            title = (h['title'] or 'No Title')[:50]
            url = h['url'][:80]
            visit_count = h['visit_count']
            domain = h['domain']
            f.write(f"| {visit_time} | {title} | {url} | {visit_count} | {domain} |\n")

    print(f"✅ Markdown出力: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Chrome閲覧履歴取得ツール')
    parser.add_argument('-f', '--format',
                       choices=['tsv', 'csv', 'json', 'md', 'all'],
                       default='tsv',
                       help='出力フォーマット (デフォルト: tsv)')
    parser.add_argument('-o', '--output',
                       default='chrome_history',
                       help='出力ファイル名（拡張子なし、デフォルト: chrome_history）')
    parser.add_argument('-l', '--limit',
                       type=int,
                       help='取得する件数の上限')
    parser.add_argument('-d', '--days',
                       type=int,
                       help='過去何日分を取得するか')
    parser.add_argument('-s', '--stats',
                       action='store_true',
                       help='統計情報を含める')

    args = parser.parse_args()

    print("🔍 Chrome履歴を取得中...")
    history = get_chrome_history(limit=args.limit, days=args.days)
    print(f"📊 {len(history)}件のレコードを取得しました")

    stats = None
    if args.stats:
        print("📈 統計情報を生成中...")
        stats = get_statistics(history)

    # 出力ディレクトリを~/tmp/に設定
    output_dir = Path.home() / "tmp"
    output_dir.mkdir(exist_ok=True)

    # 出力
    formats = ['tsv', 'csv', 'json', 'md'] if args.format == 'all' else [args.format]

    for fmt in formats:
        output_file = output_dir / f"{args.output}.{fmt}"

        if fmt == 'tsv':
            export_tsv(history, str(output_file))
        elif fmt == 'csv':
            export_csv(history, str(output_file))
        elif fmt == 'json':
            export_json(history, str(output_file), stats)
        elif fmt == 'md':
            export_markdown(history, str(output_file), stats)

if __name__ == '__main__':
    main()
