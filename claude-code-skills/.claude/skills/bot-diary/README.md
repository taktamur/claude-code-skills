# bot-diary

Obsidian Vaultにコンテンツを保存するためのスキル。YAMLフロントマターの追加、タグ規則の適用、Obsidian Publish用のフォーマット整形を自動化する。

## 機能

- YAMLフロントマター（publish、date、tags）の自動追加
- タグ規則の検証（スペース不可、CamelCase/ハイフン/アンダースコア推奨）
- 説明的なファイル名の生成（YYYY-MM-DD-トピック-説明.md）
- Obsidian Publish形式への整形

## 使い方

```
「これをbot-diaryに保存して」
「この調査結果をbot-diaryに追加して」
```

## 出力

整形されたMarkdownファイルを`~/bot-diary/`に保存。Obsidianアプリから手動で公開可能。

## 技術詳細

- [Obsidianフォーマットガイドライン](references/obsidian_format.md)
