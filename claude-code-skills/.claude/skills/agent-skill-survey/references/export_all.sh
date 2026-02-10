#!/bin/bash
# SQLiteの内容をall.mdにエクスポートするスクリプト

DB_PATH="$(dirname "$0")/references.db"
OUTPUT_PATH="$(dirname "$0")/all.md"

sqlite3 "$DB_PATH" << 'EOF' > "$OUTPUT_PATH"
.mode list
.separator "|||"

SELECT
    '# Agent Skills リファレンス一覧

SQLiteデータベースから自動生成。

- **総件数**: ' || (SELECT COUNT(*) FROM refs) || '件
- **日本語**: ' || (SELECT COUNT(*) FROM refs WHERE is_japanese = 1) || '件
- **英語**: ' || (SELECT COUNT(*) FROM refs WHERE is_japanese = 0) || '件
- **最終更新**: ' || date('now') || '

---
';

WITH tagged AS (
    SELECT
        r.url,
        r.title,
        r.published_date,
        r.surveyed_date,
        r.summary,
        r.is_japanese,
        COALESCE(GROUP_CONCAT(rt.tag, ', '), '') as tags
    FROM refs r
    LEFT JOIN ref_tags rt ON r.url = rt.url
    GROUP BY r.url
    ORDER BY COALESCE(r.published_date, r.surveyed_date) DESC, r.title
)
SELECT
    '## ' || title || '

- **日付**: ' ||
    CASE
        WHEN published_date IS NOT NULL AND published_date != ''
        THEN published_date
        ELSE '調査日 ' || surveyed_date
    END || '
- **URL**: ' || url ||
    CASE WHEN tags != '' THEN '
- **タグ**: ' || tags ELSE '' END || '
- **要約**:
  - ' || REPLACE(summary, CHAR(10), '
  - ') || '

---
'
FROM tagged;
EOF

echo "Exported to $OUTPUT_PATH"
echo "Total: $(sqlite3 "$DB_PATH" 'SELECT COUNT(*) FROM refs') entries"
