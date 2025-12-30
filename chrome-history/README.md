# chrome-history

Google Chromeの閲覧履歴を包括的に取得・分析するスキル。

## 機能

- Chrome Historyデータベースから全フィールドを抽出（URL、タイトル、訪問回数、滞在時間、遷移タイプなど）
- 複数の出力形式に対応（TSV、CSV、JSON、Markdown）
- 期間・件数指定によるフィルタリング
- 閲覧統計の生成（ドメイン別訪問数、時間帯別分布など）

## 使い方

```bash
# デフォルト（TSV形式で全履歴を取得）
python scripts/get_chrome_history.py

# 過去7日分をJSON形式で取得
python scripts/get_chrome_history.py --days 7 --format json

# 統計情報付きで全形式エクスポート
python scripts/get_chrome_history.py --format all --stats
```

## 出力

全てのファイルは `~/tmp/` ディレクトリに生成されます。

- **TSV形式**: コマンドラインツール（grep、awk等）での処理に最適（デフォルト）
- **CSV形式**: スプレッドシート分析用
- **JSON形式**: プログラム処理用、統計情報を含む
- **Markdown形式**: 人間が読みやすい表形式

## 技術詳細

- [データベーススキーマ](references/database_schema.md) - Chrome Historyデータベースの構造とクエリ例
