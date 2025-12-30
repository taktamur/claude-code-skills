---
name: chrome-history
description: Google Chromeの閲覧履歴を包括的に取得・分析するスキル。訪問時刻、URL、タイトル、訪問回数、遷移タイプ、滞在時間など全項目を抽出可能。ユーザーがChrome履歴の取得、閲覧データのエクスポート、利用パターンの分析を要求した際に使用。複数の出力形式（TSV、CSV、JSON、Markdown）と統計情報生成に対応。デフォルトはTSV形式。
accept:
  - "Bash(python scripts/get_chrome_history.py*)"
  - "Read(~/tmp/**)"
---

# Chrome閲覧履歴取得

## 概要

このスキルは、macOS上のGoogle Chromeから完全な閲覧履歴を抽出する機能を提供する。`urls`テーブルと`visits`テーブルの全フィールドを含む包括的なデータ取得が可能。複数の形式でのエクスポートと、閲覧パターンに関する統計的インサイトの生成をサポート。

**出力先**: 全てのファイルは `~/tmp/` ディレクトリに生成される（ディレクトリが存在しない場合は自動的に作成される）。

## 使用タイミング

以下のようなリクエストがあった際にこのスキルを起動する：
- 「Chromeの閲覧履歴を取得して」
- 「Chrome履歴をCSV/JSONでエクスポートして」
- 「よく訪問しているサイトを見せて」
- 「閲覧パターンを分析して」
- 「過去1週間/1ヶ月の閲覧履歴を取得して」
- Chromeの履歴データ抽出または分析に関する全てのタスク

## 主な機能

### 1. 包括的なデータ抽出

Chrome Historyデータベースから利用可能な全フィールドを抽出：

**`urls`テーブルから（URL単位の集約データ）：**
- `id` - URL固有の識別子
- `url` - 完全なURL
- `title` - ページタイトル
- `visit_count` - このURLへの総訪問回数
- `typed_count` - アドレスバーに直接入力された回数
- `last_visit_time` - 最新の訪問タイムスタンプ
- `hidden` - 非表示フラグ（真偽値）

**`visits`テーブルから（個別の訪問記録）：**
- `visit_time` - この訪問のタイムスタンプ
- `visit_duration` - ページ滞在時間（マイクロ秒）
- `transition_type` - ページへの到達方法（LINK、TYPED、RELOADなど）
- `from_visit` - リファラーの訪問ID

**追加の計算フィールド：**
- `domain` - 抽出されたドメイン名
- `visit_duration_seconds` - 秒単位の滞在時間

### 2. 複数の出力形式

以下の形式で履歴をエクスポート可能：

**TSV形式：**
- タブ区切り形式（Tab-Separated Values）
- コマンドラインツール（grep、awk、cut等）での処理に最適
- 全フィールドを列として含む
- **デフォルト形式**

**CSV形式：**
- カンマ区切り形式（Comma-Separated Values）
- スプレッドシート分析に適している（Excel、Google Sheetsなど）
- 全フィールドを列として含む

**JSON形式：**
- 統計情報を含む構造化データ
- プログラムでの処理に適している
- `--stats`フラグ使用時にメタデータを含む

**Markdown形式：**
- 人間が読みやすい形式
- フォーマット済みの表と統計情報を含む
- 上位100件のレコードとサマリーを表示

**全形式一括：**
- `--format all`で4つの形式すべてを同時にエクスポート

### 3. フィルタリングオプション

**期間指定：**
```bash
# 過去7日分を取得
python scripts/get_chrome_history.py --days 7

# 過去30日分を取得
python scripts/get_chrome_history.py --days 30
```

**件数指定：**
```bash
# 最新100件を取得
python scripts/get_chrome_history.py --limit 100

# 最新1000件を取得
python scripts/get_chrome_history.py --limit 1000
```

### 4. 統計分析

`--stats`フラグで閲覧統計を生成：

**含まれる指標：**
- 総レコード数
- ユニークURL数
- ユニークドメイン数
- 最も訪問されたドメインTop 10
- 最も訪問されたURLTop 10
- 時間帯別訪問分布（0-23時）

**使用例：**
```bash
python scripts/get_chrome_history.py --stats --format json
```

## 使用方法

### クイックスタート

最も一般的な使い方（全履歴をTSVでエクスポート）：
```bash
python scripts/get_chrome_history.py
```

これにより、利用可能な全履歴レコードを含む `~/tmp/chrome_history.tsv` が作成される。

### 完全なワークフロー

1. **出力要件を決定：**
   - 形式を選択：`--format tsv|csv|json|md|all`（デフォルト: tsv）
   - 統計情報の要否：必要なら`--stats`を追加

2. **必要に応じてフィルタを適用：**
   - 最近のデータのみ：`--days N`
   - レコード数を制限：`--limit N`

3. **スクリプトを実行：**
   ```bash
   python scripts/get_chrome_history.py \
     --format json \
     --stats \
     --days 30 \
     --output history_last_month
   ```

4. **出力を確認：**
   - `~/tmp/` ディレクトリに生成されたファイルを確認
   - ファイル名形式：`~/tmp/{出力名}.{形式}`

### 一般的な使用例

**バックアップ用に全データをエクスポート：**
```bash
python scripts/get_chrome_history.py --format all --stats
```

**最近の閲覧パターンを分析：**
```bash
python scripts/get_chrome_history.py --days 7 --format md --stats
```

**特定件数の最近の訪問を取得：**
```bash
python scripts/get_chrome_history.py --limit 500 --format tsv
```

**月次レポートを作成：**
```bash
python scripts/get_chrome_history.py --days 30 --format json --stats --output monthly_report
```

## 技術詳細

### データベースの場所（macOS）
```
~/Library/Application Support/Google/Chrome/Default/History
```

### データ処理に関する注意事項

1. **ファイルロック：** スクリプトは、Chrome実行中にファイルがロックされるため、自動的にHistoryデータベースの一時コピーを作成する。手動での介入は不要。

2. **タイムスタンプ変換：** Chromeは独自のエポック（1601-01-01）を使用。スクリプトは自動的に標準のdatetime形式に変換。

3. **遷移タイプ：** 数値の遷移コードは読みやすい名前（LINK、TYPED、RELOADなど）に変換される。

4. **複数プロファイル：** スクリプトはDefaultプロファイルから読み取る。他のプロファイルを使用する場合は、スクリプト内の`CHROME_HISTORY_PATH`を変更。

### 高度な使用方法

以下の情報については`references/database_schema.md`を参照：
- 完全なデータベーススキーマのドキュメント
- SQLクエリの例
- タイムスタンプ変換式
- 遷移タイプコードのリファレンス
- 複数プロファイル設定のガイダンス

## リソース

### scripts/get_chrome_history.py
全ての抽出、変換、エクスポート操作を実行するPythonスクリプト。コマンドライン引数で直接実行可能。

### references/database_schema.md
Chrome Historyデータベース構造の包括的なドキュメント。テーブルスキーマ、フィールドの説明、タイムスタンプ形式、SQLクエリの例を含む。
