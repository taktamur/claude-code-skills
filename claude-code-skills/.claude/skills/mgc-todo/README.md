# mgc-todo

mgc (Microsoft Graph CLI) を使用してMicrosoft To Doタスクを管理するスキル。

## 機能

- TODOリストとタスクの一覧表示
- タスクの作成、更新、完了、削除
- ステータスによるフィルタリング（未完了/進行中/完了済み）
- カレンダーや他のツールとの統合ワークフロー
- 期限付きタスクの管理

## 前提条件

```bash
# mgcのインストールと認証
mgc login --scopes User.Read Tasks.ReadWrite
```

## 使い方

```bash
# 未完了タスクを一覧表示
python scripts/mgc_todo_helper.py list-tasks --status notStarted

# タスクを作成
python scripts/mgc_todo_helper.py create-task "買い物に行く"

# 期限付きタスクを作成
python scripts/mgc_todo_helper.py create-task "レポート提出" --due-date "2025-10-30"

# タスクを完了にする
python scripts/mgc_todo_helper.py complete-task --task-id "AQMk..."
```

## 統合ワークフロー

- **カレンダー統合**: カレンダーイベントに基づいてタスクを作成・管理
- **日次計画**: 利用可能な時間に基づいてタスクを提案
- **タスク一括管理**: スクリプトで複数タスクを効率的に処理

## 技術詳細

- [MGC API リファレンス](references/mgc_api.md) - Microsoft Graph CLI の詳細なコマンドリファレンス
