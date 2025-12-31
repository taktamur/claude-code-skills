#!/usr/bin/env python3
"""
Tampermonkey Userscript一覧取得ツール

MacのChromeにインストールされているTampermonkeyのuserscriptを
LevelDBから読み取り、一覧表示する。

leveldb-cli (https://github.com/cions/leveldb-cli) を使用して
LevelDBデータベースにアクセスします。

必要なツール:
  - leveldb-cli: go install github.com/cions/leveldb-cli/cmd/leveldb@latest
"""

import json
import sys
import subprocess
from pathlib import Path
from datetime import datetime


def get_tampermonkey_db_path():
    """Tampermonkeyのデータベースパスを取得"""
    base_path = Path.home() / "Library/Application Support/Google/Chrome/Default/Local Extension Settings/dhdgffkkebhmkfjojejmpbldmpobfkfo"

    if not base_path.exists():
        return None

    return base_path


def copy_database_to_temp(db_path):
    """データベースを一時ディレクトリにコピー
    
    Chromeが起動中でもアクセスできるよう、データベースを/tmpにコピーする。
    LevelDBはLOCKファイルで保護されているため、コピーすることで
    ロック競合を回避できる。
    """
    import shutil
    import tempfile
    
    # 一時ディレクトリを作成
    temp_dir = Path(tempfile.mkdtemp(prefix="tampermonkey_db_"))
    
    try:
        # データベースディレクトリの内容をコピー
        for item in db_path.iterdir():
            if item.is_file():
                shutil.copy2(item, temp_dir / item.name)
        return temp_dir
    except Exception as e:
        print(f"エラー: データベースのコピーに失敗しました: {e}", file=sys.stderr)
        sys.exit(1)


def get_leveldb_cli_path():
    """leveldb-cliのパスを取得"""
    # ~/go/bin/leveldb を優先
    go_bin_path = Path.home() / "go/bin/leveldb"
    if go_bin_path.exists():
        return str(go_bin_path)
    
    # PATHから検索
    import shutil
    leveldb_path = shutil.which("leveldb")
    if leveldb_path:
        return leveldb_path
    
    print("エラー: leveldb-cli が見つかりません。", file=sys.stderr)
    print("以下のコマンドでインストールしてください:", file=sys.stderr)
    print("  go install github.com/cions/leveldb-cli/cmd/leveldb@latest", file=sys.stderr)
    sys.exit(1)


def leveldb_keys(db_path):
    """leveldb-cliを使ってキー一覧を取得"""
    leveldb_cli = get_leveldb_cli_path()
    
    try:
        result = subprocess.run(
            [leveldb_cli, "-d", str(db_path), "keys"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"エラー: leveldb-cli keys の実行に失敗しました: {e.stderr}", file=sys.stderr)
        sys.exit(1)


def leveldb_get(db_path, key):
    """leveldb-cliを使って値を取得"""
    leveldb_cli = get_leveldb_cli_path()
    
    try:
        result = subprocess.run(
            [leveldb_cli, "-d", str(db_path), "get", key],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError:
        # キーが存在しない場合など
        return None


def parse_scripts(db_path):
    """LevelDBからスクリプト情報を抽出"""
    scripts = {}
    
    # キー一覧を取得
    keys = leveldb_keys(db_path)
    
    # メタデータキーのみを抽出
    meta_keys = [k for k in keys if k.startswith('!extdb.@meta#')]
    
    for key in meta_keys:
        try:
            # UUIDを抽出
            uuid = key.replace('!extdb.@meta#', '')
            
            # メタデータを取得
            json_str = leveldb_get(db_path, key)
            if not json_str:
                continue
            
            meta = json.loads(json_str)
            
            if 'value' in meta and 'origin' in meta:
                value = meta['value']
                scripts[uuid] = {
                    'name': value.get('name', 'Unknown'),
                    'version': value.get('version', 'N/A'),
                    'description': value.get('description', 'N/A'),
                    'author': value.get('author', 'N/A'),
                    'enabled': value.get('enabled', False),
                    'matches': value.get('matches', []),
                    'excludes': value.get('excludes', []),
                    'grant': value.get('grant', []),
                    'position': value.get('position', 0),
                    'lastModified': value.get('lastModified', 0),
                    'uuid': uuid
                }
        except Exception:
            # パースエラーは無視
            pass
    
    return scripts


def format_timestamp(timestamp):
    """タイムスタンプをフォーマット"""
    if timestamp == 0:
        return 'N/A'
    try:
        # ミリ秒単位のタイムスタンプを秒に変換
        dt = datetime.fromtimestamp(timestamp / 1000)
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return str(timestamp)


def display_scripts(scripts):
    """スクリプト一覧を表示"""
    if not scripts:
        print("インストールされているuserscriptが見つかりませんでした。")
        return

    # ポジション順にソート
    sorted_scripts = sorted(scripts.items(), key=lambda x: x[1]['position'])

    print("=" * 80)
    print("         📦 Tampermonkey インストール済みスクリプト一覧")
    print("=" * 80)
    print()

    enabled_count = sum(1 for s in scripts.values() if s['enabled'])
    disabled_count = len(scripts) - enabled_count

    for idx, (uuid, script) in enumerate(sorted_scripts, 1):
        status = "✅ 有効" if script['enabled'] else "❌ 無効"

        print(f"【{idx}】 {script['name']}")
        print(f"     状態: {status}")
        print(f"     バージョン: v{script['version']}")
        print(f"     作者: {script['author']}")
        print(f"     説明: {script['description']}")
        print(f"     マッチ: {', '.join(script['matches']) if script['matches'] else 'なし'}")

        if script['excludes']:
            print(f"     除外: {', '.join(script['excludes'])}")

        if script['grant']:
            grant_list = ', '.join(script['grant'])
            print(f"     権限: {grant_list}")

        print(f"     最終更新: {format_timestamp(script['lastModified'])}")
        print(f"     UUID: {uuid}")
        print()

    print("=" * 80)
    print(f"合計: {len(scripts)} スクリプト (有効: {enabled_count}, 無効: {disabled_count})")
    print("=" * 80)


def main():
    """メイン処理"""
    import shutil
    
    # データベースパスを取得
    db_path = get_tampermonkey_db_path()

    if not db_path:
        print("エラー: Tampermonkeyのデータベースが見つかりません。", file=sys.stderr)
        print("以下を確認してください:", file=sys.stderr)
        print("  - Google Chromeがインストールされている", file=sys.stderr)
        print("  - Tampermonkey拡張機能がインストールされている", file=sys.stderr)
        sys.exit(1)

    # データベースを一時ディレクトリにコピー
    print("データベースをコピー中...", file=sys.stderr)
    temp_db_path = copy_database_to_temp(db_path)
    
    try:
        # スクリプト情報を抽出
        print("スクリプト情報を取得中...", file=sys.stderr)
        scripts = parse_scripts(temp_db_path)

        # 表示
        display_scripts(scripts)
    finally:
        # 一時ディレクトリを削除
        shutil.rmtree(temp_db_path, ignore_errors=True)


if __name__ == "__main__":
    main()
