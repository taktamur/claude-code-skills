#!/bin/bash
# Git リモートリポジトリの URL を取得し、HTTPS 形式に変換する

set -euo pipefail

# 引数でリポジトリパスを受け取る（省略時はカレントディレクトリ）
REPO_PATH="${1:-.}"

# リポジトリディレクトリに移動
cd "$REPO_PATH" || {
  echo "Error: リポジトリパス '$REPO_PATH' にアクセスできません" >&2
  exit 1
}

# Git リポジトリかチェック
if ! git rev-parse --git-dir > /dev/null 2>&1; then
  echo "Error: '$REPO_PATH' は Git リポジトリではありません" >&2
  exit 1
fi

# リモート URL を取得
if ! REPO_URL=$(git remote get-url origin 2>/dev/null); then
  echo "Error: リモート 'origin' が設定されていません" >&2
  exit 1
fi

# HTTPS フォーマットに変換
if [[ $REPO_URL == git@* ]]; then
  # SSH形式 (git@github.com:user/repo.git) → HTTPS形式
  REPO_URL=$(echo "$REPO_URL" | sed -e 's/:/\//' -e 's/git@/https:\/\//' -e 's/\.git$//')
elif [[ $REPO_URL == *.git ]]; then
  # HTTPS形式で .git 付き → .git を削除
  REPO_URL="${REPO_URL%.git}"
fi

# 結果を出力
echo "$REPO_URL"
