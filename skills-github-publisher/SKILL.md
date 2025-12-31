---
name: skills-github-publisher
description: Claude Code skillsをGitHub公開リポジトリに追加するスキル。スキルの内容を確認して公開可否をチェックし、.gitignoreへの追加、README.md作成、git commit/pushまでを自動化する。ユーザーが「skillをgit管理にして」「skillを公開して」などと依頼した際に使用する。
---

# Skills GitHub Publisher

## Overview

Claude Code skills を既存の GitHub リポジトリに追加し、公開するワークフローを提供する。スキルの内容確認、セキュリティチェック、README 作成、git 操作を順次実行する。

リポジトリ設定：

- **リポジトリパス**: `~/.claude/skills/`
- **リモートリポジトリ**: git remote から動的に取得（`git remote get-url origin`）
- **.gitignore 方式**: デフォルトですべてのスキルを除外し、公開対象のみを`!/<スキル名>/`で許可

## Workflow

### Step 1: スキル名の確認

ユーザーからスキル名を受け取る。スキル名が明示されていない場合は確認する。

### Step 2: スキル内容の確認

スキルディレクトリ配下のすべてのファイルを確認：

```bash
ls -la ~/.claude/skills/<スキル名>/
find ~/.claude/skills/<スキル名> -type f | sort
```

主要ファイルを読み込み：

- `SKILL.md`: スキルの説明とワークフロー
- `references/`: リファレンスファイル（存在する場合）
- その他の重要ファイル

### Step 3: 公開チェック

確認した内容から、以下をチェック：

**✅ 公開可能な内容:**

- 一般的なワークフローやテンプレート
- 公開 API の使い方
- OSS/ツールの調査方法
- 技術的なドキュメント

**❌ 公開不可な内容:**

- 機密情報（API キー、トークン、パスワード）
- 個人情報（メールアドレス、電話番号、住所）
- プライベートな設定（個人のパス、認証情報）
- 企業の機密データ
- ユーザー固有の情報（固定のリポジトリ URL、ユーザー名を含むパス、個人の設定値）

チェック結果をユーザーに報告：

```
✅ 公開可能
❌ 公開不可（理由を明記）
```

公開不可の場合はワークフローを中断。

### Step 4: .gitignore への追加

`~/.claude/skills/.gitignore`に公開対象のスキルを追加：

```gitignore
# 公開するスキル
!/book-survey/
!/oss-survey/
!/<新しいスキル名>/
```

### Step 5: スキル README.md の作成

`~/.claude/skills/<スキル名>/README.md`を作成。コンパクトな形式で以下を含める：

```markdown
# <スキル名>

<スキルの概要（1-2 文）>

## 機能

- 機能 1
- 機能 2
- 機能 3

## 使い方

\`\`\`
<使用例>
\`\`\`

## 出力

<出力の説明>

## 技術詳細

- [リファレンス 1](references/xxx.md)（存在する場合）
```

**重要**: 詳細は省き、コンパクトにまとめる。

### Step 6: ルート README.md の更新

`~/.claude/skills/README.md`のテーブルに行を追加：

```markdown
| スキル名                              | 説明                        |
| ------------------------------------- | --------------------------- |
| [book-survey](book-survey/)           | 書籍の評判を多角的に調査... |
| [oss-survey](oss-survey/)             | OSS/ツールの概要調査...     |
| [<新しいスキル名>](<新しいスキル名>/) | <簡潔な説明>                |
```

### Step 7: git 操作（add, commit, push）

変更をステージング、コミット、プッシュ：

```bash
# ステージング前に確認
git add .
git status --short

# コミット
git commit -m "$(cat <<'EOF'
feat: <スキル名>を追加

<スキルの説明>

- 機能1
- 機能2
- 機能3

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"

# プッシュ
git push
```

### Step 8: リポジトリ URL の取得

git remote からリポジトリ URL を取得：

```bash
# リモートURLを取得
REPO_URL=$(git remote get-url origin)

# HTTPSフォーマットに変換（git@形式の場合）
if [[ $REPO_URL == git@* ]]; then
  REPO_URL=$(echo "$REPO_URL" | sed -e 's/:/\//' -e 's/git@/https:\/\//' -e 's/\.git$//')
elif [[ $REPO_URL == *.git ]]; then
  REPO_URL="${REPO_URL%.git}"
fi
```

リモートが設定されていない場合はエラーを報告してワークフローを中断。

### Step 9: 完了報告

ユーザーに以下を報告：

- 公開チェック結果
- 追加されたファイル一覧
- コミットハッシュ
- リポジトリ URL（Step 8 で取得した動的 URL）
- スキルの公開 URL: `${REPO_URL}/tree/main/<スキル名>`

## Notes

- セキュリティチェックは必須。疑わしい内容がある場合は公開を中断
- README.md は簡潔に。詳細は SKILL.md に記載されているため重複を避ける
- git 操作の前に必ず`git status`で確認
- コミットメッセージは統一された形式を使用
