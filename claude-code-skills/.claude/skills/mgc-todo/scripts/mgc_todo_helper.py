#!/usr/bin/env python3
"""
MGC TODO ヘルパースクリプト

mgc (Microsoft Graph CLI) コマンドを使用してMicrosoft To Doタスクを管理するための
便利なラッパー関数を提供する。

必要要件:
- mgc CLIがインストールされ、認証されていること
- ログインコマンド: mgc login --scopes User.Read Tasks.ReadWrite

使用例:
    # すべてのTODOリストを一覧表示
    python mgc_todo_helper.py list-lists

    # デフォルトリストからタスクを一覧表示
    python mgc_todo_helper.py list-tasks

    # 特定のリストからタスクを一覧表示
    python mgc_todo_helper.py list-tasks --list-id "AQMk..."

    # 未完了タスクのみを一覧表示
    python mgc_todo_helper.py list-tasks --status notStarted

    # 新しいタスクを作成
    python mgc_todo_helper.py create-task "買い物に行く"

    # 説明付きでタスクを作成
    python mgc_todo_helper.py create-task "買い物に行く" --body "牛乳と卵を買う"

    # タスクを完了にする
    python mgc_todo_helper.py complete-task --task-id "AQMk..."

    # タスクのタイトルを更新
    python mgc_todo_helper.py update-task --task-id "AQMk..." --title "新しいタイトル"

    # タスクを削除
    python mgc_todo_helper.py delete-task --task-id "AQMk..."
"""

import sys
import json
import subprocess
import argparse
from typing import Optional, List, Dict, Any


def run_mgc_command(args: List[str]) -> Dict[str, Any]:
    """
    mgcコマンドを実行し、パースされたJSON出力を返す。

    Args:
        args: mgcに渡すコマンド引数

    Returns:
        mgcからのパースされたJSONレスポンス

    Raises:
        subprocess.CalledProcessError: mgcコマンドが失敗した場合
        json.JSONDecodeError: 出力が有効なJSONでない場合
    """
    try:
        result = subprocess.run(
            ["mgc"] + args,
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"mgcコマンド実行エラー: {e.stderr}", file=sys.stderr)
        raise
    except json.JSONDecodeError as e:
        print(f"JSONパースエラー: {e}", file=sys.stderr)
        print(f"生の出力: {result.stdout}", file=sys.stderr)
        raise


def get_default_list_id() -> str:
    """
    デフォルトTODOリストのIDを取得する。

    Returns:
        デフォルトTODOリストのリストID

    Raises:
        ValueError: デフォルトリストが見つからない場合
    """
    lists_data = run_mgc_command(["me", "todo", "lists", "list"])

    for todo_list in lists_data.get("value", []):
        if todo_list.get("wellknownListName") == "defaultList":
            return todo_list["id"]

    raise ValueError("デフォルトTODOリストが見つかりません")


def list_todo_lists() -> Dict[str, Any]:
    """
    すべてのTODOリストを一覧表示する。

    Returns:
        すべてのTODOリストを含む辞書
    """
    return run_mgc_command(["me", "todo", "lists", "list"])


def list_tasks(list_id: Optional[str] = None, status: Optional[str] = None) -> Dict[str, Any]:
    """
    TODOリストからタスクを一覧表示する。

    Args:
        list_id: TODOリストのID（デフォルトはデフォルトリスト）
        status: ステータスでフィルタ (notStarted, inProgress, completed)

    Returns:
        タスクを含む辞書
    """
    if list_id is None:
        list_id = get_default_list_id()

    tasks_data = run_mgc_command([
        "me", "todo", "lists", "tasks", "list",
        "--todo-task-list-id", list_id
    ])

    # ステータスが指定されている場合はフィルタ
    if status:
        tasks_data["value"] = [
            task for task in tasks_data.get("value", [])
            if task.get("status") == status
        ]

    return tasks_data


def create_task(
    title: str,
    list_id: Optional[str] = None,
    body: Optional[str] = None,
    due_date: Optional[str] = None
) -> Dict[str, Any]:
    """
    新しいタスクを作成する。

    Args:
        title: タスクのタイトル
        list_id: TODOリストのID（デフォルトはデフォルトリスト）
        body: タスクの説明/本文
        due_date: 期限日（ISO形式、例: "2025-10-25"）

    Returns:
        作成されたタスクを含む辞書
    """
    if list_id is None:
        list_id = get_default_list_id()

    # タスクオブジェクトを構築
    task_obj = {
        "title": title
    }

    if body:
        task_obj["body"] = {
            "content": body,
            "contentType": "text"
        }

    if due_date:
        task_obj["dueDateTime"] = {
            "dateTime": f"{due_date}T00:00:00.0000000",
            "timeZone": "UTC"
        }

    # mgcコマンドを使用してタスクを作成
    result = subprocess.run(
        [
            "mgc", "me", "todo", "lists", "tasks", "create",
            "--todo-task-list-id", list_id,
            "--body", json.dumps(task_obj)
        ],
        capture_output=True,
        text=True,
        check=True
    )

    return json.loads(result.stdout)


def update_task(
    task_id: str,
    list_id: Optional[str] = None,
    title: Optional[str] = None,
    body: Optional[str] = None,
    status: Optional[str] = None
) -> Dict[str, Any]:
    """
    既存のタスクを更新する。

    Args:
        task_id: 更新するタスクのID
        list_id: TODOリストのID（デフォルトはデフォルトリスト）
        title: 新しいタスクタイトル
        body: 新しいタスク説明/本文
        status: 新しいステータス (notStarted, inProgress, completed)

    Returns:
        更新されたタスクを含む辞書
    """
    if list_id is None:
        list_id = get_default_list_id()

    # 更新オブジェクトを構築
    update_obj = {}

    if title:
        update_obj["title"] = title

    if body:
        update_obj["body"] = {
            "content": body,
            "contentType": "text"
        }

    if status:
        update_obj["status"] = status

    # mgcコマンドを使用してタスクを更新
    result = subprocess.run(
        [
            "mgc", "me", "todo", "lists", "tasks", "patch",
            "--todo-task-list-id", list_id,
            "--todo-task-id", task_id,
            "--body", json.dumps(update_obj)
        ],
        capture_output=True,
        text=True,
        check=True
    )

    return json.loads(result.stdout)


def complete_task(task_id: str, list_id: Optional[str] = None) -> Dict[str, Any]:
    """
    タスクを完了としてマークする。

    Args:
        task_id: 完了にするタスクのID
        list_id: TODOリストのID（デフォルトはデフォルトリスト）

    Returns:
        更新されたタスクを含む辞書
    """
    return update_task(task_id, list_id, status="completed")


def delete_task(task_id: str, list_id: Optional[str] = None) -> None:
    """
    タスクを削除する。

    Args:
        task_id: 削除するタスクのID
        list_id: TODOリストのID（デフォルトはデフォルトリスト）
    """
    if list_id is None:
        list_id = get_default_list_id()

    subprocess.run(
        [
            "mgc", "me", "todo", "lists", "tasks", "delete",
            "--todo-task-list-id", list_id,
            "--todo-task-id", task_id
        ],
        check=True
    )


def main():
    """ヘルパースクリプトのメインCLIインターフェース。"""
    parser = argparse.ArgumentParser(
        description="MGC TODO ヘルパー - Microsoft To Do操作の便利なラッパー"
    )

    subparsers = parser.add_subparsers(dest="command", help="実行するコマンド")

    # list-lists コマンド
    subparsers.add_parser("list-lists", help="すべてのTODOリストを一覧表示")

    # list-tasks コマンド
    list_tasks_parser = subparsers.add_parser("list-tasks", help="タスクを一覧表示")
    list_tasks_parser.add_argument("--list-id", help="TODOリストID（デフォルトはデフォルトリスト）")
    list_tasks_parser.add_argument("--status", choices=["notStarted", "inProgress", "completed"],
                                   help="タスクステータスでフィルタ")

    # create-task コマンド
    create_task_parser = subparsers.add_parser("create-task", help="新しいタスクを作成")
    create_task_parser.add_argument("title", help="タスクのタイトル")
    create_task_parser.add_argument("--list-id", help="TODOリストID（デフォルトはデフォルトリスト）")
    create_task_parser.add_argument("--body", help="タスクの説明/本文")
    create_task_parser.add_argument("--due-date", help="期限日（ISO形式、例: 2025-10-25）")

    # update-task コマンド
    update_task_parser = subparsers.add_parser("update-task", help="タスクを更新")
    update_task_parser.add_argument("--task-id", required=True, help="更新するタスクID")
    update_task_parser.add_argument("--list-id", help="TODOリストID（デフォルトはデフォルトリスト）")
    update_task_parser.add_argument("--title", help="新しいタスクタイトル")
    update_task_parser.add_argument("--body", help="新しいタスク説明/本文")
    update_task_parser.add_argument("--status", choices=["notStarted", "inProgress", "completed"],
                                    help="新しいタスクステータス")

    # complete-task コマンド
    complete_task_parser = subparsers.add_parser("complete-task", help="タスクを完了としてマーク")
    complete_task_parser.add_argument("--task-id", required=True, help="完了にするタスクID")
    complete_task_parser.add_argument("--list-id", help="TODOリストID（デフォルトはデフォルトリスト）")

    # delete-task コマンド
    delete_task_parser = subparsers.add_parser("delete-task", help="タスクを削除")
    delete_task_parser.add_argument("--task-id", required=True, help="削除するタスクID")
    delete_task_parser.add_argument("--list-id", help="TODOリストID（デフォルトはデフォルトリスト）")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        if args.command == "list-lists":
            result = list_todo_lists()
            print(json.dumps(result, indent=2, ensure_ascii=False))

        elif args.command == "list-tasks":
            result = list_tasks(args.list_id, args.status)
            print(json.dumps(result, indent=2, ensure_ascii=False))

        elif args.command == "create-task":
            result = create_task(args.title, args.list_id, args.body, args.due_date)
            print(json.dumps(result, indent=2, ensure_ascii=False))

        elif args.command == "update-task":
            result = update_task(
                args.task_id, args.list_id, args.title, args.body, args.status
            )
            print(json.dumps(result, indent=2, ensure_ascii=False))

        elif args.command == "complete-task":
            result = complete_task(args.task_id, args.list_id)
            print(json.dumps(result, indent=2, ensure_ascii=False))

        elif args.command == "delete-task":
            delete_task(args.task_id, args.list_id)
            print("タスクが正常に削除されました")

    except Exception as e:
        print(f"エラー: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
