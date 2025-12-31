# Skills GitHub Publisher

Claude Code skillsを既存のGitHubリポジトリに追加し、公開するワークフローを自動化するスキルです。

## 機能

- スキル内容の確認とセキュリティチェック
- .gitignoreへの自動追加
- スキルREADME.mdの自動生成
- ルートREADME.mdのテーブル更新
- git commit/pushの自動実行

## 使い方

```
skills-github-publisherをgit管理にして
```

```
book-surveyスキルを公開して
```

## ワークフロー

1. スキル名の確認
2. スキル内容の確認（SKILL.md、referencesなど）
3. 公開チェック（機密情報、個人情報がないか）
4. .gitignoreへの追加
5. スキルREADME.mdの作成
6. ルートREADME.mdのテーブル更新
7. git add, commit, push
8. 完了報告

## リポジトリ設定

- リポジトリパス: `~/.claude/skills/`
- リモートリポジトリ: git remoteから動的に取得
- .gitignore方式: デフォルトですべて除外し、公開対象のみ許可

**注**: リポジトリURLは実行時に`git remote get-url origin`で取得されます。
