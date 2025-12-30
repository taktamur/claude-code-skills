---
name: mgc-todo
description: mgc (Microsoft Graph CLI) コマンドを使用してMicrosoft To Doタスクを管理するスキル。TODOリストやタスクの操作、カレンダーなど他ツールとのTODO管理統合が必要な場合に使用。タスクの一覧表示、作成、更新、完了、削除をサポート。日々の活動計画、カレンダーイベントとTODOタスクの組み合わせ、タスクワークフローの管理に特に有用。
---

# MGC TODO マネージャー

## 概要

mgc (Microsoft Graph CLI) コマンドラインツールを使用してMicrosoft To Doタスクを管理する。このスキルは、一般的なTODO操作のワークフローとヘルパーツールを提供し、カレンダー計画、プロジェクト管理、日常活動の調整など、他のワークフローとタスク管理を簡単に統合できるようにする。

## このスキルを使用するタイミング

以下の場合にこのスキルを使用する：
- TODOタスクやリストを一覧表示する
- タスクを作成、更新、完了する
- TODOをカレンダーや他ツールと統合する
- 利用可能な時間に基づいて日々の活動を計画する
- プログラム的にタスクワークフローを管理する
- タスクの一括操作（フィルタリング、複数タスクの更新）

**一般的なシナリオ:**
- 「今日のTODOタスクを表示して」
- 「食料品を買うタスクを作成して」
- 「『レポート完成』タスクを完了にして」
- 「次の2時間でできるタスクは何？」
- 「明日のカレンダーイベントに基づいてタスクを追加して」

## 前提条件

このスキルを使用する前に、mgcがインストールされ認証されていることを確認する：

```bash
# mgcのインストール（まだの場合）
# 参照: https://learn.microsoft.com/en-us/graph/cli/installation

# 必要なスコープで認証
mgc login --scopes User.Read Tasks.ReadWrite
```

## 主要な操作

### 1. TODOリストの一覧表示

利用可能なすべてのTODOリストを表示する：

```bash
mgc me todo lists list
```

デフォルトリストはレスポンスに `"wellknownListName": "defaultList"` が含まれている。

**ヘルパースクリプトを使用する場合:**
```bash
python scripts/mgc_todo_helper.py list-lists
```

**一般的なワークフロー:**
1. すべてのTODOリストを一覧表示
2. 名前または `wellknownListName` で目的のリストを特定
3. 後続の操作で使用するために `id` フィールドを抽出
4. デフォルトリストで作業する場合、ヘルパースクリプトを使用すると自動的に検出される

### 2. タスクの一覧表示

**デフォルトリストからすべてのタスクを一覧表示:**
```bash
python scripts/mgc_todo_helper.py list-tasks
```

**特定のリストからタスクを一覧表示:**
```bash
python scripts/mgc_todo_helper.py list-tasks --list-id "AQMk..."
```

**ステータスでフィルタ:**
```bash
# 未完了タスクのみ
python scripts/mgc_todo_helper.py list-tasks --status notStarted

# 完了済みタスクのみ
python scripts/mgc_todo_helper.py list-tasks --status completed

# 進行中タスク
python scripts/mgc_todo_helper.py list-tasks --status inProgress
```

**mgcコマンドを直接使用:**
```bash
mgc me todo lists tasks list --todo-task-list-id "<list-id>"
```

**jqでフィルタリング:**
```bash
# 高優先度の未完了タスク
mgc me todo lists tasks list --todo-task-list-id "<list-id>" | \
  jq '.value[] | select(.status == "notStarted" and .importance == "high")'

# 今日または期限切れのタスク
TODAY=$(date -u +%Y-%m-%d)
mgc me todo lists tasks list --todo-task-list-id "<list-id>" | \
  jq --arg today "$TODAY" '.value[] | select(.dueDateTime.dateTime <= $today)'
```

### 3. タスクの作成

**シンプルなタスク:**
```bash
python scripts/mgc_todo_helper.py create-task "買い物に行く"
```

**説明付きタスク:**
```bash
python scripts/mgc_todo_helper.py create-task "買い物に行く" --body "牛乳と卵を買う"
```

**期限付きタスク:**
```bash
python scripts/mgc_todo_helper.py create-task "レポート提出" --due-date "2025-10-30"
```

**今日のタスクとして作成（今日の期限を設定）:**
```bash
# 今日の日付を期限に設定することで、Microsoft To Doアプリで今日が期限のタスクとして表示される
python scripts/mgc_todo_helper.py create-task "掃除" --due-date "2025-11-22"
```

**特定のリストにタスクを作成:**
```bash
python scripts/mgc_todo_helper.py create-task "プロジェクト会議準備" --list-id "AQMk..."
```

**mgcで高度なタスク作成:**
```bash
mgc me todo lists tasks create --todo-task-list-id "<list-id>" --body '{
  "title": "プロジェクト会議",
  "body": {
    "content": "Q4の進捗報告を準備",
    "contentType": "text"
  },
  "importance": "high",
  "isReminderOn": true,
  "reminderDateTime": {
    "dateTime": "2025-10-25T09:00:00.0000000",
    "timeZone": "Asia/Tokyo"
  },
  "dueDateTime": {
    "dateTime": "2025-10-25T14:00:00.0000000",
    "timeZone": "Asia/Tokyo"
  }
}'
```

### 4. タスクの更新

**タイトルを更新:**
```bash
python scripts/mgc_todo_helper.py update-task --task-id "AQMk..." --title "新しいタイトル"
```

**説明を更新:**
```bash
python scripts/mgc_todo_helper.py update-task --task-id "AQMk..." --body "更新された説明"
```

**ステータスを変更:**
```bash
python scripts/mgc_todo_helper.py update-task --task-id "AQMk..." --status inProgress
```

**複数フィールドを更新:**
```bash
python scripts/mgc_todo_helper.py update-task \
  --task-id "AQMk..." \
  --title "更新されたタスク" \
  --body "新しい説明" \
  --status inProgress
```

### 5. タスクの完了

**完了としてマーク:**
```bash
python scripts/mgc_todo_helper.py complete-task --task-id "AQMk..."
```

**update-taskを使用:**
```bash
python scripts/mgc_todo_helper.py update-task --task-id "AQMk..." --status completed
```

### 6. タスクの削除

```bash
python scripts/mgc_todo_helper.py delete-task --task-id "AQMk..."
```

## 統合ワークフロー

### ワークフロー1: カレンダーと組み合わせた日次計画

TODOとカレンダーイベントを組み合わせる場合：

1. **今日のカレンダーイベントを取得**（カレンダーツール/スキルを使用）
2. **未完了のTODOタスクを一覧表示:**
   ```bash
   python scripts/mgc_todo_helper.py list-tasks --status notStarted
   ```
3. **カレンダーイベント間の利用可能時間を分析**
4. **利用可能な時間枠に収まるタスクを提案**
5. **必要に応じて新しいタスクを作成**（カレンダーの予定に基づく）
6. **カレンダーの緊急度に基づいてタスクの優先度を更新**

**プロンプト例:** 「今日のカレンダーとTODOリストを表示して、空き時間に完了できるタスクを提案して」

### ワークフロー2: タスク完了レビュー

1日または1週間の終わりに：

1. **完了したタスクを一覧表示:**
   ```bash
   python scripts/mgc_todo_helper.py list-tasks --status completed
   ```
2. **達成事項をレビュー**
3. **残りの未完了タスクを一覧表示:**
   ```bash
   python scripts/mgc_todo_helper.py list-tasks --status notStarted
   ```
4. **残りのタスクの優先度を再設定またはスケジュール変更**

### ワークフロー3: タスクの一括管理

複数のタスクを管理する場合：

1. **すべてのタスクを一覧表示**し、必要に応じてフィルタ
2. **タスクIDを抽出**（jqなどのツールを使用）
3. **タスクをループ処理**して一括操作:
   ```bash
   # 例: すべての期限切れタスクを高優先度としてマーク
   mgc me todo lists tasks list --todo-task-list-id "<list-id>" | \
     jq -r '.value[] | select(.dueDateTime.dateTime < now | todate) | .id' | \
     while read task_id; do
       python scripts/mgc_todo_helper.py update-task \
         --task-id "$task_id" \
         --importance high
     done
   ```

### ワークフロー4: コンテキストベースのタスク作成

メール、会議、メモからタスクを作成する場合：

1. **ソースからタスク情報を抽出**
2. **適切なリストを決定**（デフォルトまたは特定）
3. **コンテキスト付きでタスクを作成:**
   ```bash
   python scripts/mgc_todo_helper.py create-task \
     "クライアントにフォローアップ" \
     --body "件名: 今日の会議でのプロジェクト提案の議論" \
     --due-date "2025-10-28"
   ```
4. **時間的制約がある場合はリマインダーを設定**

## ヘルパースクリプトリファレンス

`scripts/mgc_todo_helper.py` スクリプトは一般的な操作の便利なラッパーを提供する：

**コマンド:**
- `list-lists` - すべてのTODOリストを一覧表示
- `list-tasks` - オプションのフィルタリング付きでタスクを一覧表示
- `create-task` - 新しいタスクを作成
- `update-task` - タスクプロパティを更新
- `complete-task` - タスクを完了としてマーク
- `delete-task` - タスクを削除

**主な機能:**
- 指定がない場合、デフォルトリストIDを自動的に検出
- mgcコマンドのJSON形式を処理
- ステータスによるフィルタリング提供
- 明確なCLIインターフェースで一般的な操作を簡素化

**完全な使用方法を表示:**
```bash
python scripts/mgc_todo_helper.py --help
```

## 高度なトピック

### チェックリストアイテムの操作

タスクにはサブタスク（チェックリストアイテム）を持つことができる。詳細なAPIリファレンスは `references/mgc_api.md` を参照。

**チェックリストアイテムを一覧表示:**
```bash
mgc me todo lists tasks checklist-items list \
  --todo-task-list-id "<list-id>" \
  --todo-task-id "<task-id>"
```

**チェックリストアイテムを作成:**
```bash
mgc me todo lists tasks checklist-items create \
  --todo-task-list-id "<list-id>" \
  --todo-task-id "<task-id>" \
  --body '{"displayName": "サブタスク1"}'
```

### 「今日の予定」（My Day）への対応

**重要な制限事項:**
Microsoft To Doの「今日の予定」（My Day）機能は、Microsoft Graph API（mgcが使用）で直接サポートされていません（2024年時点）。APIを通じて直接タスクを「今日の予定」に追加することはできません。

**回避策:**
タスクを今日のタスクとして扱いたい場合は、`dueDateTime`を今日の日付に設定します：

```bash
# 今日の日付（例: 2025-11-22）を期限に設定
python scripts/mgc_todo_helper.py create-task "掃除" --due-date "2025-11-22"
python scripts/mgc_todo_helper.py create-task "洗濯" --due-date "2025-11-22"
```

この方法により：
- Microsoft To Doアプリで今日が期限のタスクとして表示される
- タスクが今日完了すべきものとして明確になる
- 必要に応じて、アプリから手動で「今日の予定」に追加できる

**複数のタスクを一度に作成する例:**
```bash
# 日常的なタスクを今日の期限で作成
for task in "掃除" "洗濯" "食器洗い"; do
  python scripts/mgc_todo_helper.py create-task "$task" --due-date "$(date +%Y-%m-%d)"
done
```

### 日付と時刻の処理

すべての日付はISO 8601形式を使用：

**日付のみ:** `"2025-10-25"`

**DateTimeオブジェクト:**
```json
{
  "dateTime": "2025-10-25T09:00:00.0000000",
  "timeZone": "Asia/Tokyo"
}
```

**一般的なタイムゾーン:**
- `UTC` - 協定世界時
- `Asia/Tokyo` - 日本標準時
- `America/New_York` - 東部標準時

### パフォーマンスの考慮事項

- **ページネーション:** 大きなタスクリストはページ分割される；レスポンスの `@odata.nextLink` を確認
- **レート制限:** 過度に急速なAPI呼び出しを避ける
- **キャッシング:** API呼び出しを減らすためリストIDのキャッシュを検討
- **一括操作:** 個別呼び出しではなく、一括操作にはスクリプトを使用

## リソース

### scripts/mgc_todo_helper.py

mgc TODO操作の便利なラッパー関数を提供するPythonヘルパースクリプト。以下を含む：
- デフォルトリストの自動検出
- 簡略化されたコマンドラインインターフェース
- mgcコマンドのJSON処理
- ステータスフィルタリング機能

直接実行するか、カスタムスクリプトで関数をインポートして使用。

### references/mgc_api.md

mgc TODOコマンドの包括的なリファレンスドキュメント。以下を含む：
- 完全なコマンド構文
- レスポンス構造の詳細
- jqを使用した高度なフィルタリング
- エラーハンドリングパターン
- ベストプラクティスと一般的なパターン
- APIの制限と考慮事項

複雑な操作に詳細なAPI情報が必要な場合にこのリファレンスを読み込む。

## トラブルシューティング

**認証エラー:**
```bash
# 適切なスコープで再認証
mgc login --scopes User.Read Tasks.ReadWrite
```

**リストIDが見つからない:**
- リストが存在することを確認: `mgc me todo lists list`
- リストIDのタイポをチェック
- ヘルパースクリプトを使用してデフォルトリストを自動検出

**タスクが更新されない:**
- タスクIDが正しいことを確認
- 書き込み権限があることをチェック
- mgcコマンドでJSON形式が有効であることを確認

**日付形式エラー:**
- ISO 8601形式を使用: 日付は `YYYY-MM-DD`
- DateTimeオブジェクトにはタイムゾーンを含める
- 日付/時刻フィールドの適切なJSON構造を確認

## ベストプラクティス

1. **一般的な操作にはヘルパースクリプトを使用**して複雑さを軽減
2. **可能な限りデフォルトリストで作業**してリストID管理を回避
3. **ステータスと重要度を使用して早期にタスクをフィルタ**して処理を削減
4. **時間的制約のあるタスクには期限を設定**して優先度付けを改善
5. **明確なタイトルを使用**してタスクを明確に説明
6. **コンテキスト付きの説明を追加**して後でタスクを実行可能にする
7. **他のツールと組み合わせる**（カレンダー、メール）包括的な生産性向上のため
8. **定期的にレビュー**してタスクリストを最新かつ関連性のある状態に保つ
