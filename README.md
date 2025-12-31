# Claude Code Skills

[Claude Code](https://claude.com/claude-code)で使用できるスキルのコレクションです。

**注意**: これらのスキルは個人的に使うために作ったものです。そのため、そのまま使うというよりも、これらからアイデアを得る/コピーして自分用のスキルの土台として使う、のが良いと思います。

## 公開スキル

| スキル名 | 説明 |
|---------|------|
| [agent-skill-survey](agent-skill-survey/) | Agent Skillsの活用事例を調査・収集し、使用パターンを分析。Zenn、GitHub、技術ブログなどから情報収集し、SQLiteで管理。 |
| [book-survey](book-survey/) | 書籍の評判を多角的に調査し、構造化されたMarkdownレポートを生成。ポジティブ・ネガティブ両面のレビュー収集、国立国会図書館APIで書影取得。 |
| [bot-diary](bot-diary/) | Obsidian Vaultにコンテンツを保存。YAMLフロントマター追加、タグ規則適用、Obsidian Publish用フォーマット整形を自動化。 |
| [chrome-history](chrome-history/) | Google Chromeの閲覧履歴を包括的に取得・分析。TSV/CSV/JSON/Markdown形式でエクスポート、統計情報生成に対応。 |
| [homebrew-cask-security](homebrew-cask-security/) | Homebrew caskの定義ファイルを取得・分析し、インストール前に悪意のあるコードや疑わしい設定がないかをセキュリティチェック。 |
| [mgc-todo](mgc-todo/) | mgc (Microsoft Graph CLI) を使用してMicrosoft To Doタスクを管理。リスト/タスクの操作、カレンダー統合ワークフローを提供。 |
| [oss-survey](oss-survey/) | OSS/ツールの概要調査を実施し、構造化されたMarkdownレポートを生成。基本情報、競合比較、日本語サポート状況の調査。 |
| [scrapbox-monthly-page](scrapbox-monthly-page/) | Scrapbox用の月次ページを生成。指定年月の全日付と曜日をScrapboxリンク形式で出力、前後月へのナビゲーションリンクも含む。 |
| [skills-github-publisher](skills-github-publisher/) | Claude Code skillsをGitHubリポジトリに追加・公開。セキュリティチェック、README生成、git操作を自動化。 |
| [tampermonkey-list](tampermonkey-list/) | MacのChromeにインストールされているTampermonkey userscriptの一覧を取得・表示。メタデータ（名前、バージョン、作者、有効/無効状態）を確認可能。 |

## スキルの使い方

### 方法1: GitHubからダウンロード

1. このリポジトリのページで「Code」ボタンをクリック
2. 「Download ZIP」を選択してダウンロード
3. zipファイルを展開
4. 使いたいスキルのディレクトリを`~/.claude/skills/`にコピー

```bash
# 例: book-surveyスキルを使う場合
cp -r claude-code-skills-main/book-survey ~/.claude/skills/
```

### 方法2: git clone

```bash
# リポジトリをクローン
git clone <このリポジトリのURL>

# 使いたいスキルをコピー
cp -r claude-code-skills/book-survey ~/.claude/skills/
```

## カスタマイズについて

公開されているスキルには、作者固有の設定が含まれている場合があります。使用する際は、以下の点を確認し、必要に応じて変更してください。

**変更が必要な可能性がある設定:**
- **保存先パス**: `~/bot-diary/`などのデフォルト保存先
- **リポジトリURL**: GitHubリポジトリのURL
- **ファイル名形式**: 出力ファイルの命名規則

**変更方法:**
各スキルの`SKILL.md`を開き、該当する設定値を自分の環境に合わせて編集してください。

## ライセンス

CC0 1.0 Universal - 詳細は[LICENSE](LICENSE)を参照してください。

このプロジェクトはパブリックドメインです。自由に使用、改変、配布できます。
