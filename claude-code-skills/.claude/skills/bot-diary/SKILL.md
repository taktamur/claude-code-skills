---
name: bot-diary
description: コンテンツをbot-diary Obsidian Vaultに保存する。YAMLフロントマター追加、タグ規則適用を行い、Obsidian Publish用に整形して保存する。
---

# Bot Diary

## 概要

bot-diaryは、LLM生成ドキュメントのリポジトリとして機能するObsidian Vaultである。すべての記事は、Obsidian Publishを通じて公開される。

このスキルは、任意のMarkdownコンテンツをbot-diary Vault形式に整形して保存する機能を提供する。

**Vaultディレクトリ**: `~/bot-diary`

## このスキルを使用するタイミング

以下の場合にこのスキルを使用する：
- 既に作成したコンテンツをbot-diaryに保存したい
- 調査結果、まとめ、記事をbot-diary形式で保存したい
- work-session-documenterスキルから呼び出される

典型的なユーザーリクエスト：
- 「これをbot-diaryに保存して」
- 「この調査結果をbot-diaryに追加して」
- （調査・まとめ作業後に）「bot-diaryに保存して」

## Vault情報

- **Vaultパス**: `~/bot-diary`
- **目的**: LLM生成ドキュメントのアーカイブと公開

## 保存機能

このスキルは以下の処理を行う：

### 1. YAMLフロントマターの追加

すべての記事に必須のフロントマターを追加する：

```yaml
---
publish: true
date: YYYY-MM-DD
tags:
  - Tag1
  - Tag2
---
```

### 2. タグ規則の適用

**重要**: タグにスペースを含めてはいけない。

✅ **使用可能**:
- CamelCase: `ObsidianPublish`
- ハイフン区切り: `obsidian-publish`
- アンダースコア: `obsidian_publish`

❌ **使用禁止**: `Obsidian Publish`（スペースがあると解析エラー）

### 3. ファイル名の生成

記事は説明的なファイル名で保存される：

**推奨パターン**:
- `YYYY-MM-DD-トピック-説明.md`
- 例：`2025-11-02-obsidian-publish-setup.md`

### 4. Vaultへの保存

整形したMarkdownファイルを `/Users/tak/bot-diary/` に保存する。

## フォーマット要件

### 必須フロントマター

- `publish: true` - 公開用マーク（ただし手動公開は引き続き必要）
- `date: YYYY-MM-DD` - 記事の日付
- `tags:` - 関連するトピックタグ（スペース不可）

### コンテンツガイドライン

- 主に日本語で記述する
- Markdownフォーマットを使用する
- 言語識別子付きのコードブロックを含める
- 関連する場合は `[[記事名]]` 構文で内部リンクを追加する
- 情報的で技術的なトーンを維持する

### よくある落とし穴

❌ **避ける**：スペースを含むタグ（例：`Obsidian Publish`）
✅ **使用する**：`ObsidianPublish` または `obsidian-publish`

❌ **避ける**：フロントマターの欠落
✅ **使用する**：すべての記事に完全なYAMLフロントマター

## 公開ワークフロー

記事保存後、ユーザーは以下の手順でObsidianアプリから手動で公開する：

1. Obsidianアプリを開く
2. `⌘+P` でコマンドパレットを開く
3. 「パブリッシュによる変更の公開」を選択
4. 公開するファイルを選択
5. 「パブリッシュ」ボタンをクリック

**注意**: `publish: true` が設定されていても、ファイルは自動的に公開されません。Obsidianアプリでの手動選択が必要です。

## リソース

### references/obsidian_format.md

以下に関する詳細ドキュメントが含まれています：
- YAMLフロントマターのフォーマット仕様
- タグ命名規則と制限
- ファイル命名パターン
- コンテンツ構造ガイドライン
- 完全な公開ワークフロー
- Vault情報とURL

Obsidian固有のフォーマット要件や公開手順について明確化が必要な場合は、このファイルを参照してください。

## 関連スキル

- **work-session-documenter**: 作業セッションを記録する際にこのスキルを呼び出す
