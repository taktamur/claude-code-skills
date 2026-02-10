---
name: github-repo-jobutsu
description: privateかつarchive済みのGitHubリポジトリを調査し、Scrapbox形式の記事を生成するスキル。ユーザーが「ネタ成仏して」「アーカイブリポジトリを調べて」「GitHubのリポジトリを整理して」などと依頼した際に使用する。
allowed-tools: Bash(gh *), Bash(git log *), Bash(rm -rf ~/tmp/github-repo-jobutsu/*), Bash(cat ~/tmp/github-repo-jobutsu/output.txt | pbcopy), Bash(mkdir *)
---

# Skill: ネタ成仏 - GitHubアーカイブリポジトリ調査 & Scrapbox記事生成

## 概要
privateかつarchive済みのGitHubリポジトリを調査し、Scrapbox形式の記事を生成するスキル。

## 前提条件
- `gh` コマンドが認証済みであること
- `git` コマンドが利用可能であること
- `~/tmp/github-repo-jobutsu/` ディレクトリを作業用に使用する

## 手順

### Step 1: 対象リポジトリ一覧の取得
```bash
gh repo list --private --archived --limit 200 --json name,createdAt,updatedAt,url --jq 'sort_by(.createdAt) | .[] | [.name, .createdAt[:10], .updatedAt[:10], .url] | @tsv'
```

取得結果を以下の形式でユーザーに提示し、番号で選択してもらう:
```
| No. | リポジトリ名 | 作成日 | 最終更新日 | URL |
|-----|------------|--------|-----------|-----|
| 1   | repo-name  | 2020-01-01 | 2023-12-31 | https://github.com/<ユーザ名>/repo-name |
| 2   | ...        | ...    | ...       | ... |
```

ユーザーが番号を指定したら、該当リポジトリを対象としてStep 2に進む。

### Step 2: リポジトリのチェックアウト
作業ディレクトリがなければ作成し、対象リポジトリをクローンする。
```bash
mkdir -p ~/tmp/github-repo-jobutsu
gh repo clone <ユーザ名>/<リポジトリ名> ~/tmp/github-repo-jobutsu/<リポジトリ名>
```

### Step 3: リポジトリの調査
以下を読み取って情報を収集する:
- README.md
- ファイル構成（Globで全ファイル一覧）
- ソースコードのヘッダファイルや主要ファイル
- git log（コミット履歴）
- リポジトリのメタデータ（primaryLanguage, description等）

収集する情報:
- リポジトリ名
- 作成日
- 最終更新日
- URL
- 技術キーワード（使用言語、フレームワーク、主要技術）
- 概要（何をするものか、含まれる機能）
- コアソース（プロジェクトの本質的なロジックを含むファイルを特定し、内容を抽出する）
  - 設定ファイル、ボイラープレート（AppDelegate等）、自動生成コードは除外
  - エントリポイントや核心的な処理を含むファイルを選定

### Step 4: Scrapbox形式で出力
以下のテンプレートに従って整形する:

```
ネタ成仏_<リポジトリ名>
[public.icon]
#ネタ成仏_不要となったgithubのリポジトリ

🤖
 リポジトリ名: <リポジトリ名>
 作成日: [YYYY/MM/DD]
 最終更新日: [YYYY/MM/DD]
 URL: <リポジトリURL>
 技術キーワード: [キーワード1] [キーワード2] ...
 概要
  <概要文（キーワードになりそうな箇所を[]で括る）>
  <機能説明（キーワードになりそうな箇所を[]で括る）>
 コアソース
code:<ファイル名>
 <ソースコード（各行を半角スペース1つでインデント）>
```

### Step 5: クリップボードにコピー
生成したScrapbox形式のテキストを `~/tmp/github-repo-jobutsu/output.txt` にWriteツールで書き出し、以下のコマンドでクリップボードにコピーする。
```bash
cat ~/tmp/github-repo-jobutsu/output.txt | pbcopy
```

## 出力フォーマットルール
- 1行目: `ネタ成仏_<リポジトリ名>`（ページタイトル）
- 2行目: `[public.icon]`
- 3行目: `#ネタ成仏_不要となったgithubのリポジトリ`（ハッシュタグ）
- 4行目: 空行
- 5行目: `🤖`
- 6行目以降: 半角スペースによるインデントで箇条書き
- 日付は `[YYYY/MM/DD]` 形式で `[]` で括る
- 技術キーワードは各項目を `[]` で括る
- 概要文中のキーワード（技術用語、ライブラリ名、フレームワーク名、固有名詞等）も `[]` で括る
- コアソースはScrapboxのコードブロック記法（`code:ファイル名` + 各行を半角スペース1つでインデント）で記載
  - ボイラープレート（AppDelegate等）、設定ファイル、自動生成コードは含めない
  - プロジェクトの本質的な処理を含むファイルのみ抜粋
  - 複数ファイルがある場合はそれぞれ `code:ファイル名` で記載
  - **空行（改行のみの行）は省略する**（Scrapboxの `code:` ブロック内で空行があると表示が崩れるため）

## 後処理
調査完了後、クローンしたリポジトリとoutput.txtを削除する:
```bash
rm -rf ~/tmp/github-repo-jobutsu/<リポジトリ名>
rm -f ~/tmp/github-repo-jobutsu/output.txt
```
