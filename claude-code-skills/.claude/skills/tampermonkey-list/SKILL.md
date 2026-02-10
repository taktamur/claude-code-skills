---
name: tampermonkey-list
description: MacのChromeにインストールされているTampermonkey userscriptの一覧を取得し、スクリプト名、有効/無効状態、バージョン、作者などのメタデータを表示する。ユーザーが「Tampermonkeyのスクリプトを確認して」「userscriptの一覧を見せて」などのリクエストをした際に使用する。
---

# Tampermonkey Userscript一覧取得

## 目的

MacのChromeにインストールされているTampermonkeyのuserscript一覧を取得し、スクリプトのメタデータを整形して表示する。

## 使用タイミング

このスキルは、ユーザーが以下のようなリクエストを行った際に使用する：

- 「Tampermonkeyにインストールされているスクリプトを確認して」
- 「userscriptの一覧を表示して」
- 「Tampermonkeyのスクリプトを調べて」
- 「どんなuserscriptが入ってるか教えて」

## 実行方法

### 1. 前提条件を確認

以下の環境が整っていることを確認する：

- macOS環境
- Google Chrome
- Tampermonkey拡張機能がインストール済み
- `leveldb-cli`がインストール済み（未インストールの場合は `go install github.com/cions/leveldb-cli/cmd/leveldb@latest` を実行）

### 2. スクリプト一覧を取得

`scripts/list_scripts.py` を実行してスクリプト一覧を取得する：

```bash
python3 scripts/list_scripts.py
```

このスクリプトは以下を実行する：

1. TampermonkeyのLevelDBデータベースを一時ディレクトリにコピー
   - 元のパス: `~/Library/Application Support/Google/Chrome/Default/Local Extension Settings/dhdgffkkebhmkfjojejmpbldmpobfkfo/`
   - Chromeが起動中でもアクセスできるようにコピーを使用
2. `leveldb-cli` ([leveldb-cli](https://github.com/cions/leveldb-cli)) を使用してデータを読み取り
   - `leveldb keys` でキー一覧を取得
   - `leveldb get` で各キーの値を取得
3. メタデータ（`!extdb.@meta#<UUID>`キー）を抽出・パース
4. スクリプト情報を整形して表示
5. 一時ディレクトリをクリーンアップ

### 3. 結果の表示

スクリプトは以下の情報を含む整形済みリストを出力する：

- スクリプト名
- 有効/無効状態（✅/❌）
- バージョン
- 作者
- 説明
- マッチパターン
- 除外パターン
- 権限（grant）
- 最終更新日時
- UUID

出力例：

```
================================================================================
         📦 Tampermonkey インストール済みスクリプト一覧
================================================================================

【1】 GPT Summary Button with API
     状態: ✅ 有効
     バージョン: v1.1
     作者: taktamur
     説明: Display a summary button that uses GPT to summarize the page content
     マッチ: *://*/*
     権限: none
     最終更新: 2024-08-14 20:14:13
     UUID: 89b18d77-9e02-4883-a15f-6445e12eee8b

================================================================================
合計: 1 スクリプト (有効: 1, 無効: 0)
================================================================================
```

## データ構造

TampermonkeyはLevelDB形式でデータを保存している：

- **保存場所**: `~/Library/Application Support/Google/Chrome/Default/Local Extension Settings/dhdgffkkebhmkfjojejmpbldmpobfkfo/`
- **フォーマット**: LevelDB
- **キーの種類**: 
  - `!extdb.@meta#<UUID>`: スクリプトのメタデータ
  - `!extdb.@source#<UUID>`: スクリプトのソースコード
- **値**: JSON形式のデータ

## トラブルシューティング

### leveldb-cliがインストールされていない場合

以下のコマンドでインストールする：

```bash
go install github.com/cions/leveldb-cli/cmd/leveldb@latest
```

インストール後、`~/go/bin/leveldb`が利用可能になります。

### データベースが見つからない場合

以下を確認する：

- Chromeのプロファイルを確認（"Default"以外のProfileを使用している可能性）
- Tampermonkeyがインストールされているか確認
- Chromeを再起動してみる

## 注意事項

- このスキルはmacOS + Chrome環境専用
- Tampermonkeyの拡張機能ID `dhdgffkkebhmkfjojejmpbldmpobfkfo` に依存
- データは読み取り専用で、変更は行わない
- LevelDBの読み取りには`leveldb-cli`を使用
- データベースのロック競合を避けるため、一時ディレクトリにコピーしてアクセス

## 関連ファイル

- `scripts/list_scripts.py`: スクリプト一覧取得用Pythonスクリプト
