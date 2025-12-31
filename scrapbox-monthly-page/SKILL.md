---
name: scrapbox-monthly-page
description: Scrapbox用の月次ページを生成するスキル。指定した年月の全日付と曜日をScrapboxリンク形式で出力し、前後の月へのナビゲーションリンクも含む。ユーザーが「Scrapboxの月次ページを作って」「2025年1月の月ページを生成して」「来月分のScrapboxカレンダーページを作成して」などと依頼した際に使用する。
---

# Scrapbox Monthly Page Generator

指定した年月のScrapbox形式の月次ページを生成する。

## 使用方法

`scripts/generate.py` を実行して月次ページを生成する。

```bash
python3 scripts/generate.py YYYY-MM
```

例:
```bash
python3 scripts/generate.py 2025-11
```

## 出力フォーマット

```
2025/11
[2025/10] ← →[2025/12]

[2025/11/01](土)
[2025/11/02](日)
...
[2025/11/30](日)
```

## フォーマット仕様

- タイトル行: `YYYY/MM`
- ナビゲーション: `[前月] ← →[翌月]`（Scrapboxリンク形式）
- 日付行: `[YYYY/MM/DD](曜日) `（末尾にスペース1つ、Scrapboxリンク形式）
- 曜日: 日本語1文字（月火水木金土日）
