# tampermonkey-list

MacのChromeにインストールされているTampermonkey userscriptの一覧を取得し、スクリプト名、有効/無効状態、バージョン、作者などのメタデータを表示するClaude Codeスキルです。

## 機能

- TampermonkeyのLevelDBデータベースからuserscript一覧を取得
- スクリプトのメタデータ（名前、バージョン、作者、説明）を表示
- 有効/無効状態、マッチパターン、権限情報を確認
- Chrome起動中でもアクセス可能（一時ディレクトリにコピーして読み取り）

## 使い方

Claude Codeで以下のように依頼：

```
「Tampermonkeyのスクリプト一覧を表示して」
「userscriptを確認して」
「Tampermonkeyに何がインストールされてる？」
```

または直接スクリプトを実行：

```bash
python3 ~/.claude/skills/tampermonkey-list/scripts/list_scripts.py
```

## 前提条件

- macOS
- Google Chrome
- Tampermonkey拡張機能
- `leveldb-cli` ([leveldb-cli](https://github.com/cions/leveldb-cli))

インストール方法：

```bash
go install github.com/cions/leveldb-cli/cmd/leveldb@latest
```

## 出力例

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

## 技術詳細

詳細は [SKILL.md](SKILL.md) を参照してください。

- Tampermonkeyのデータベース構造
- LevelDBの読み取り方法
- トラブルシューティング
