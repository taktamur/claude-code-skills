# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

Claude Code スキルのコレクション（個人用）。GNU Stow でシンボリックリンク管理し、`~/.claude/skills/` に配置する。ライセンスは CC0（パブリックドメイン）。

## コマンド

```bash
# スキルのシンボリックリンクを作成（インストール）
mise run setup
# または: stow -v -t ~ claude-code-skills

# シンボリックリンクを削除（アンインストール）
mise run teardown

# シンボリックリンクを再作成（更新時）
mise run restow
```

## ディレクトリ構成

```
claude-code-skills/          # Stow パッケージ（この中が ~ にシンボリックリンクされる）
  .claude/
    skills/
      <スキル名>/
        SKILL.md             # スキル定義（必須）
        README.md            # 概要説明
        scripts/             # ヘルパースクリプト（任意）
        references/          # 追加ドキュメント（任意）
```

Stow の仕組み上、`claude-code-skills/.claude/skills/*` が `~/.claude/skills/*` にシンボリックリンクされる。

## スキル（SKILL.md）の構造

SKILL.md は以下の YAML フロントマターで始まる：

```yaml
---
name: スキル名
description: スキルの説明文（Claude Code のスキル一覧に表示される）
---
```

本文は日本語で記述し、以下のセクションを含める：
- 目的 / Overview
- 使用タイミング（トリガーとなるユーザーリクエスト例）
- 実行方法（前提条件、手順）

## コミットメッセージ規約

Conventional Commits に準拠：`feat:`, `fix:`, `docs:`, `refactor:` など。メッセージは日本語。
