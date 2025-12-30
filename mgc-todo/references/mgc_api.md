# Microsoft Graph CLI (mgc) - TODO API リファレンス

このドキュメントは、mgc CLIを使用してMicrosoft To Doを操作するためのリファレンス情報を提供します。

## 前提条件

### 認証

mgcコマンドを使用する前に、必要なスコープで認証を行います：

```bash
mgc login --scopes User.Read Tasks.ReadWrite
```

**必須スコープ:**
- `User.Read` - ユーザープロファイル情報の読み取り
- `Tasks.ReadWrite` - To Doタスクへの読み書きアクセス

**オプショナルスコープ:**
- `Tasks.Read` - 読み取り専用アクセス（書き込みアクセスが不要な場合）
- `Calendars.ReadWrite` - カレンダーアクセス（統合用）
- `Mail.ReadWrite` - メールアクセス（統合用）

## コマンド構造

すべてのTODO関連コマンドは以下のパターンに従います：

```
mgc me todo [リソース] [アクション] [オプション]
```

## TODOリスト

### すべてのTODOリストを一覧表示

```bash
mgc me todo lists list
```

**レスポンス構造:**
```json
{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users(...)/todo/lists",
  "value": [
    {
      "@odata.etag": "W/\"...\"",
      "displayName": "タスク",
      "isOwner": true,
      "isShared": false,
      "wellknownListName": "defaultList",
      "id": "AQMk..."
    }
  ]
}
```

**主要フィールド:**
- `id` - リストの一意識別子（他の操作に必要）
- `displayName` - 人が読めるリスト名
- `wellknownListName` - システムリストの特別な識別子（`defaultList`、`flaggedEmails`、または `none`）
- `isOwner` - 現在のユーザーがこのリストを所有しているかどうか
- `isShared` - リストが他のユーザーと共有されているかどうか

### 特定のリストを取得

```bash
mgc me todo lists get --todo-task-list-id "<list-id>"
```

### 新しいリストを作成

```bash
mgc me todo lists create --body '{"displayName": "新しいリスト"}'
```

### リストを更新

```bash
mgc me todo lists patch --todo-task-list-id "<list-id>" --body '{"displayName": "更新されたリスト名"}'
```

### リストを削除

```bash
mgc me todo lists delete --todo-task-list-id "<list-id>"
```

## タスク

### リスト内のタスクを一覧表示

```bash
mgc me todo lists tasks list --todo-task-list-id "<list-id>"
```

**レスポンス構造:**
```json
{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users(...)/todo/lists(...)/tasks",
  "value": [
    {
      "@odata.etag": "W/\"...\"",
      "importance": "normal",
      "isReminderOn": false,
      "status": "notStarted",
      "title": "タスクのタイトル",
      "createdDateTime": "2025-10-21T00:19:24.9444767Z",
      "lastModifiedDateTime": "2025-10-21T00:19:25.0628516Z",
      "hasAttachments": false,
      "categories": [],
      "id": "AQMk...",
      "body": {
        "content": "タスクの詳細",
        "contentType": "text"
      },
      "dueDateTime": {
        "dateTime": "2025-10-25T00:00:00.0000000",
        "timeZone": "UTC"
      }
    }
  ]
}
```

**主要フィールド:**
- `id` - タスクの一意識別子
- `title` - タスクタイトル（必須）
- `status` - タスクステータス: `notStarted`、`inProgress`、`completed`、`waitingOnOthers`、`deferred`
- `importance` - 優先度: `low`、`normal`、`high`
- `body.content` - タスクの説明/メモ
- `body.contentType` - コンテンツ形式: `text` または `html`
- `isReminderOn` - リマインダーが設定されているかどうか
- `reminderDateTime` - リマインダーのトリガー時刻
- `dueDateTime` - タスクの期限日時
- `completedDateTime` - タスクが完了した時刻（ステータスが `completed` の場合）
- `categories` - カテゴリ名の配列
- `hasAttachments` - タスクに添付ファイルがあるかどうか
- `checklistItems` - チェックリストアイテム（サブタスク）の配列

### 特定のタスクを取得

```bash
mgc me todo lists tasks get --todo-task-list-id "<list-id>" --todo-task-id "<task-id>"
```

### 新しいタスクを作成

**基本的なタスク:**
```bash
mgc me todo lists tasks create --todo-task-list-id "<list-id>" --body '{
  "title": "新しいタスク"
}'
```

**説明と期限付きのタスク:**
```bash
mgc me todo lists tasks create --todo-task-list-id "<list-id>" --body '{
  "title": "買い物に行く",
  "body": {
    "content": "牛乳と卵を買う",
    "contentType": "text"
  },
  "dueDateTime": {
    "dateTime": "2025-10-25T00:00:00.0000000",
    "timeZone": "UTC"
  },
  "importance": "high"
}'
```

**リマインダー付きのタスク:**
```bash
mgc me todo lists tasks create --todo-task-list-id "<list-id>" --body '{
  "title": "ミーティング準備",
  "isReminderOn": true,
  "reminderDateTime": {
    "dateTime": "2025-10-25T09:00:00.0000000",
    "timeZone": "UTC"
  }
}'
```

### タスクを更新

```bash
mgc me todo lists tasks patch --todo-task-list-id "<list-id>" --todo-task-id "<task-id>" --body '{
  "title": "更新されたタイトル",
  "status": "inProgress"
}'
```

**タスクを完了にする:**
```bash
mgc me todo lists tasks patch --todo-task-list-id "<list-id>" --todo-task-id "<task-id>" --body '{
  "status": "completed"
}'
```

**重要度を更新:**
```bash
mgc me todo lists tasks patch --todo-task-list-id "<list-id>" --todo-task-id "<task-id>" --body '{
  "importance": "high"
}'
```

### タスクを削除

```bash
mgc me todo lists tasks delete --todo-task-list-id "<list-id>" --todo-task-id "<task-id>"
```

## チェックリストアイテム

タスクにはチェックリストアイテム（サブタスク）を持つことができます。

### チェックリストアイテムを一覧表示

```bash
mgc me todo lists tasks checklist-items list --todo-task-list-id "<list-id>" --todo-task-id "<task-id>"
```

### チェックリストアイテムを作成

```bash
mgc me todo lists tasks checklist-items create --todo-task-list-id "<list-id>" --todo-task-id "<task-id>" --body '{
  "displayName": "サブタスク1"
}'
```

### チェックリストアイテムを更新

```bash
mgc me todo lists tasks checklist-items patch --todo-task-list-id "<list-id>" --todo-task-id "<task-id>" --checklist-item-id "<item-id>" --body '{
  "isChecked": true
}'
```

### チェックリストアイテムを削除

```bash
mgc me todo lists tasks checklist-items delete --todo-task-list-id "<list-id>" --todo-task-id "<task-id>" --checklist-item-id "<item-id>"
```

## フィルタリングとクエリ

### jqを使用したフィルタリング

`jq` コマンドラインツールはJSON出力のフィルタリングに便利です：

**タスクのタイトルのみを取得:**
```bash
mgc me todo lists tasks list --todo-task-list-id "<list-id>" | jq '.value[].title'
```

**未完了タスクをフィルタ:**
```bash
mgc me todo lists tasks list --todo-task-list-id "<list-id>" | jq '.value[] | select(.status == "notStarted")'
```

**高優先度タスクをフィルタ:**
```bash
mgc me todo lists tasks list --todo-task-list-id "<list-id>" | jq '.value[] | select(.importance == "high")'
```

**期限のあるタスクを取得:**
```bash
mgc me todo lists tasks list --todo-task-list-id "<list-id>" | jq '.value[] | select(.dueDateTime != null)'
```

**完了タスクをカウント:**
```bash
mgc me todo lists tasks list --todo-task-list-id "<list-id>" | jq '[.value[] | select(.status == "completed")] | length'
```

**デフォルトリストIDを検索:**
```bash
mgc me todo lists list | jq '.value[] | select(.wellknownListName == "defaultList") | .id'
```

## 一般的なパターン

### デフォルトリストの検索

ほとんどの操作はデフォルトのTODOリストで動作します。IDを取得するには：

```bash
DEFAULT_LIST_ID=$(mgc me todo lists list | jq -r '.value[] | select(.wellknownListName == "defaultList") | .id')
```

### すべての一般的なフィールドを含むタスクの作成

```bash
mgc me todo lists tasks create --todo-task-list-id "<list-id>" --body '{
  "title": "完全なタスク例",
  "body": {
    "content": "詳細な説明がここに入ります",
    "contentType": "text"
  },
  "importance": "high",
  "isReminderOn": true,
  "reminderDateTime": {
    "dateTime": "2025-10-25T09:00:00.0000000",
    "timeZone": "UTC"
  },
  "dueDateTime": {
    "dateTime": "2025-10-25T17:00:00.0000000",
    "timeZone": "UTC"
  },
  "categories": ["仕事", "重要"]
}'
```

### バッチ操作

複数のタスクを更新するには、シェルループを使用します：

```bash
# すべてのnotStartedタスクをinProgressにマーク
for task_id in $(mgc me todo lists tasks list --todo-task-list-id "<list-id>" | jq -r '.value[] | select(.status == "notStarted") | .id'); do
  mgc me todo lists tasks patch --todo-task-list-id "<list-id>" --todo-task-id "$task_id" --body '{"status": "inProgress"}'
done
```

## 日付と時刻の形式

すべての日付と時刻はISO 8601形式を使用します：

**日付のみ:**
```
"2025-10-25"
```

**日時（dueDateTime、reminderDateTimeなど）:**
```json
{
  "dateTime": "2025-10-25T09:00:00.0000000",
  "timeZone": "UTC"
}
```

**一般的なタイムゾーン:**
- `UTC` - 協定世界時
- `Asia/Tokyo` - 日本標準時
- `America/New_York` - 東部標準時
- `Europe/London` - 英国時間

## エラーハンドリング

### よくあるエラー

**認証エラー:**
```
Error: Unauthorized - Please run 'mgc login --scopes User.Read Tasks.ReadWrite'
```
**解決策:** 適切なスコープで再認証します。

**無効なリストID:**
```
Error: Resource not found
```
**解決策:** `mgc me todo lists list` を使用してリストIDが正しいことを確認します。

**無効なJSON:**
```
Error: Invalid JSON in --body parameter
```
**解決策:** JSONが適切にフォーマットされ、シェルコマンドでエスケープされていることを確認します。

### ベストプラクティス

1. **操作を実行する前に常にリストIDを検証**
2. **可能な限りデフォルトリストを使用**して操作を簡素化
3. **大きなタスクリストのページネーションを処理**（レスポンスの `@odata.nextLink` を確認）
4. **よく使用するIDを変数または設定ファイルに保存**
5. **JSON出力のフィルタリングと変換にjqを使用**
6. **レート制限を避けるためバッチ操作を慎重に実行**

## 制限事項

- **レート制限:** Microsoft Graph APIにはレート制限があり、過度のリクエストはスロットルされる可能性があります
- **ページネーション:** 大きな結果セットはページ分割されます；レスポンスの `@odata.nextLink` を確認してください
- **添付ファイル:** ファイルの添付には別のAPI呼び出しが必要です
- **繰り返し:** 繰り返しタスクにはより複雑な設定が必要です
- **共有リスト:** 共有リストでは一部の操作が制限される場合があります
