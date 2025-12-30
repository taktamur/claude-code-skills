# Claude Code Skills

[Claude Code](https://claude.com/claude-code)で使用できるスキルのコレクションです。

## 公開スキル

| スキル名 | 説明 |
|---------|------|
| [agent-skill-survey](agent-skill-survey/) | Agent Skillsの活用事例を調査・収集し、使用パターンを分析。Zenn、GitHub、技術ブログなどから情報収集し、SQLiteで管理。 |
| [book-survey](book-survey/) | 書籍の評判を多角的に調査し、構造化されたMarkdownレポートを生成。ポジティブ・ネガティブ両面のレビュー収集、国立国会図書館APIで書影取得。 |
| [oss-survey](oss-survey/) | OSS/ツールの概要調査を実施し、構造化されたMarkdownレポートを生成。基本情報、競合比較、日本語サポート状況の調査。 |
| [skills-github-publisher](skills-github-publisher/) | Claude Code skillsをGitHubリポジトリに追加・公開。セキュリティチェック、README生成、git操作を自動化。 |

## スキルの使い方

1. [リポジトリをzipでダウンロード](https://github.com/taktamur/claude-code-skills/archive/refs/heads/main.zip)
2. zipファイルを展開
3. 使いたいスキルのディレクトリを`~/.claude/skills/`にコピー

```bash
# 例: book-surveyスキルを使う場合
cp -r claude-code-skills-main/book-survey ~/.claude/skills/
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

MIT License - 詳細は[LICENSE](LICENSE)を参照してください。

Copyright (c) 2025 [taktamur](https://github.com/taktamur)
