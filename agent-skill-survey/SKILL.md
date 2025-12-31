---
name: agent-skill-survey
description: Agent Skillsの活用事例を様々なソース（Zenn、GitHub、技術ブログなど）から調査・収集し、使用パターンを分析してまとめるスキル。ユーザーが「agent skillの事例を調べて」「agent skillの使い方を調査して」などと依頼した際に使用する。
approvedTools:
  - WebSearch:*
  - WebFetch:*
  - Write:~/tmp/*
  - Bash:sqlite3:*
  - Bash:./references/export_all.sh:*
---

# Agent Skill Survey

このスキルは、Agent Skills の活用事例を調査・収集し、使用パターンを分析してまとめる。

## 使用タイミング

以下のような依頼があった場合に使用：

- 「agent skill の活用事例を調べて」
- 「agent skill の使い方を調査して」
- 「agent skills の使用例を探して」
- 「どんな agent skills が使われているか調べて」
- 「agent skill 事例を追加調査して」
- 「agent skill 事例を更新して」
- 「agent skill の DB を更新して」

## 調査の進め方

### 1. 情報源の選択

**検索対象期間**: 直近 1 ヶ月を重点的にターゲットとする（`after:YYYY-MM-DD`形式で日付フィルタを使用）

以下のソースから調査を行う：

- **Zenn**: 日本語の技術記事
  - 例: `Claude agent skills after:2025-12-01 site:zenn.dev`
- **Qiita**: 日本語の技術記事
  - 例: `Claude agent skills after:2025-12-01 site:qiita.com`
- **note.com**: 日本語の実践的な記事
  - 例: `Claude agent skills after:2025-12-01 site:note.com`
- **はてなブログ**: 日本語の技術ブログ
  - 例: `Claude agent skills after:2025-12-01 site:hatenablog.com`
- **GitHub**:
  - リポジトリ検索、マーケットプレイス
  - SKILL.md ファイルの検索
  - 例: `agent skills Claude after:2025-12-01 site:github.com SKILL.md`
- **Hacker News**: 技術的な議論とコメント
  - 例: `Claude agent skills after:2025-12-01 site:news.ycombinator.com`
- **Dev.to**: 英語の技術記事
  - 例: `Claude agent skills after:2025-12-01 site:dev.to`
- **公式ドキュメント**: Anthropic 公式のサンプルとベストプラクティス

**除外**: Medium（WebFetch でエラーが出るため）、X/Twitter（WebFetch で内容取得不可）

**日付フィルタの計算方法**:

- 調査実行日から 1 ヶ月前の日付を計算（例: 2025-12-30 なら `after:2025-12-01`）
- 検索クエリに必ず日付フィルタを含める

### 2. 情報の収集

各記事から以下の情報を抽出：

- **タイトル**: 記事のタイトル
- **日付**: 公開日または更新日
- **要約**: 主な内容、作成されたスキルの概要、使用パターン
- **URL**: 記事へのリンク

### 3. リファレンスの更新

収集した情報は**SQLite データベース**に記録する（重複チェック・タグ検索が可能）。

#### データベースへの追加

```sql
-- 重複チェック（追加前に必ず実行）
SELECT * FROM refs WHERE url = 'https://...';

-- 新規追加（要約は改行区切りで複数行可）
INSERT INTO refs (url, title, published_date, surveyed_date, summary, is_japanese)
VALUES (
    'https://zenn.dev/...',
    '記事タイトル',
    '2025-12-25',        -- 公開日（不明ならNULL）
    '2025-12-25',        -- 調査日（必須）
    '1行目の要約ポイント
2行目の要約ポイント
3行目の要約ポイント',   -- 改行で区切ると箇条書きで出力される
    1                    -- 日本語:1, 英語:0
);

-- タグ追加（任意）
INSERT INTO tags (name) VALUES ('new-tag') ON CONFLICT DO NOTHING;
INSERT INTO ref_tags (url, tag) VALUES ('https://...', 'new-tag');
```

#### 利用可能なタグ

```sql
SELECT name FROM tags ORDER BY name;
-- 用途別: business, collaboration, creative, data-analysis, dev-tools,
--         document-processing, productivity, security, writing
-- 特徴別: progressive-disclosure, skill-creator, tutorial, comparison,
--         obsidian, ml-training, tdd, subagent, mcp, official,
--         curated-list, enterprise, document-skills, git-workflow, open-standard
```

#### Markdown 出力

```bash
# all.md を再生成
./references/export_all.sh
```

#### キュレーションリポジトリからの一括登録

awesome-claude-skills のようなキュレーションリポジトリから個別スキルを一括登録する場合は、ハイブリッド方式を使用する：

1. **README からスキル情報を抽出**（Python スクリプト）
2. **一時ファイルに SQL 生成**（レビュー用）
3. **内容確認後、DB に一括 INSERT**
4. **export_all.sh で Markdown 再生成**

```python
# ~/tmp/extract_skills.py のテンプレート
SKILLS = [
    # (name, url, description, category)
    ("docx", "https://github.com/anthropics/skills/tree/main/document-skills/docx",
     "Create, edit, analyze Word docs with tracked changes.", "document-processing"),
    # ... 他のスキル
]

# SQL生成: INSERT OR IGNORE で重複を自動スキップ
# タグ: カテゴリタグ + curated-list を付与
```

実行手順：

```bash
# 1. スクリプト実行でSQL生成
python3 ~/tmp/extract_skills.py

# 2. 生成されたSQLをレビュー
cat ~/tmp/awesome_skills_insert.sql

# 3. DBに一括INSERT
sqlite3 references/references.db < ~/tmp/awesome_skills_insert.sql

# 4. Markdown再生成
./references/export_all.sh
```

### 4. パターンの分析

収集した事例から使用パターンを分類：

- 情報検索・調査系
- ドキュメント・ノート管理系
- 専門的な提案・計画系
- ユーティリティ系
- 企業・チームでの導入事例

### 5. all.md の再生成

データベース更新後、Markdown 出力を再生成：

```bash
./references/export_all.sh
```

### 6. 結果のまとめ

調査結果をユーザーに報告する際は：

- 発見した活用事例の概要
- 使用パターンの分類
- 特に興味深い実装例
- 参考リンクの提示

## リファレンス構成

```
references/
├── references.db      # SQLiteデータベース（メイン）
├── all.md             # 全件出力（export_all.shで生成）
└── export_all.sh      # Markdown出力スクリプト
```

### SQLite スキーマ

```sql
-- メインテーブル
CREATE TABLE refs (
    url TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    published_date TEXT,
    surveyed_date TEXT NOT NULL,
    summary TEXT,
    is_japanese INTEGER DEFAULT 1,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- タグ
CREATE TABLE tags (name TEXT PRIMARY KEY);
CREATE TABLE ref_tags (
    url TEXT, tag TEXT,
    PRIMARY KEY (url, tag)
);
```

### GUI で確認

DB Browser for SQLite で直接確認できる：

```bash
open -a "/Applications/DB Browser for SQLite.app" references/references.db
```

### 便利なクエリ

```sql
-- ソース別件数（URLから自動判定）
SELECT
  CASE
    WHEN url LIKE '%zenn.dev%' THEN 'zenn'
    WHEN url LIKE '%github.com%' THEN 'github'
    WHEN url LIKE '%claude.com%' OR url LIKE '%anthropic.com%' THEN 'official'
    ELSE 'blog'
  END as source, COUNT(*)
FROM refs GROUP BY source;

-- タグで検索
SELECT r.title, r.url FROM refs r
JOIN ref_tags rt ON r.url = rt.url
WHERE rt.tag = 'progressive-disclosure';

-- 最近追加した記事
SELECT title, surveyed_date FROM refs ORDER BY surveyed_date DESC LIMIT 10;
```

## 注意事項

- 調査は薄く広く行い、詳細な実装には深入りしない
- 各記事の要約は簡潔に（3-5 行程度）
- **新規追加時は必ず SQLite に登録**（URL で自動重複チェック）
- `export_all.sh`で Markdown を再生成可能
- ユーザーの要望に応じて、特定のソースやタグに絞った調査も可能
