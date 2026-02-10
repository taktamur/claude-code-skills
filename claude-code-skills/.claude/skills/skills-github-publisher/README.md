# Skills GitHub Publisher

Claude Code skillsをGNU Stow管理のGitHubリポジトリに追加し、公開するワークフローを自動化するスキルです。

## 機能

- スキル内容の確認とセキュリティチェック
- Stowパッケージへのスキル移動（ローカルスキルの場合）
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

1. スキル名の確認とStowチェック
2. スキル内容の確認（SKILL.md、referencesなど）
3. 公開チェック（機密情報、個人情報がないか）
4. スキルREADME.mdの作成
5. ルートREADME.mdのテーブル更新
6. git add, commit, push
7. リポジトリURL取得（`gh repo view`）
8. 完了報告
