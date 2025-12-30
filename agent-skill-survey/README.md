# agent-skill-survey

Agent Skillsの活用事例を様々なソース（Zenn、GitHub、技術ブログなど）から調査・収集し、使用パターンを分析してまとめるスキル。

## 機能

- 直近1ヶ月の技術記事・リポジトリから Agent Skills の活用事例を収集
- WebSearch/WebFetch を使用した多様なソースからの情報収集（Zenn、Qiita、GitHub、公式ドキュメントなど）
- SQLite データベースによる重複チェック機能付きリファレンス管理
- タグベースの分類とMarkdown形式での出力

## 使い方

```
agent skillの事例を調べて
agent skillの使い方を調査して
```

## 出力

- SQLite データベース（`references/references.db`）に記録
- Markdown形式の一覧（`references/all.md`）を自動生成
- ソース別、タグ別の集計と分類

## 技術詳細

- データベーススキーマ（refs、tags、ref_tags テーブル）
- 日付フィルタによる直近情報の優先的な収集
- キュレーションリポジトリからの一括登録サポート
