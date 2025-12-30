# Chrome履歴データベーススキーマ

Chrome の履歴は SQLite データベースに保存されています。

## データベースの場所

**macOS:**
```
~/Library/Application Support/Google/Chrome/Default/History
```

**Windows:**
```
%LOCALAPPDATA%\Google\Chrome\User Data\Default\History
```

**Linux:**
```
~/.config/google-chrome/Default/History
```

## 主要テーブル

### urls テーブル

URL ごとの集約情報を保存。

| カラム名 | 型 | 説明 |
|---------|---|------|
| id | INTEGER PRIMARY KEY | URL の一意な ID |
| url | LONGVARCHAR | 完全な URL |
| title | LONGVARCHAR | ページタイトル |
| visit_count | INTEGER | このURLへの総訪問回数 |
| typed_count | INTEGER | アドレスバーに直接入力された回数 |
| last_visit_time | INTEGER | 最後の訪問時刻（Chrome エポック） |
| hidden | INTEGER | 非表示フラグ（0 or 1） |

### visits テーブル

個々の訪問記録を保存。

| カラム名 | 型 | 説明 |
|---------|---|------|
| id | INTEGER PRIMARY KEY | 訪問の一意な ID |
| url | INTEGER | urls.id への外部キー |
| visit_time | INTEGER | 訪問時刻（Chrome エポック） |
| from_visit | INTEGER | 前の訪問の ID（リファラー） |
| transition | INTEGER | 遷移タイプ（下記参照） |
| segment_id | INTEGER | セッション ID |
| visit_duration | INTEGER | 滞在時間（マイクロ秒） |

## Chromeタイムスタンプ

Chrome は独自のエポック（1601-01-01 00:00:00 UTC）を使用します。

**変換式（Python）:**
```python
unix_timestamp = chrome_timestamp / 1000000 - 11644473600
datetime_obj = datetime.fromtimestamp(unix_timestamp)
```

## 遷移タイプ (transition)

`transition` カラムは下位 8 ビットがコアタイプを示します。

| 値 | 名前 | 説明 |
|----|------|------|
| 0 | LINK | リンクのクリック |
| 1 | TYPED | アドレスバーに入力 |
| 2 | AUTO_BOOKMARK | ブックマークの自動的な使用 |
| 3 | AUTO_SUBFRAME | サブフレームの自動ナビゲーション |
| 4 | MANUAL_SUBFRAME | サブフレームの手動ナビゲーション |
| 5 | GENERATED | 生成されたナビゲーション |
| 6 | START_PAGE | スタートページ |
| 7 | FORM_SUBMIT | フォーム送信 |
| 8 | RELOAD | ページのリロード |
| 9 | KEYWORD | キーワード検索 |
| 10 | KEYWORD_GENERATED | キーワード生成 |

## データ取得時の注意

1. **ファイルロック**: Chrome が実行中の場合、History ファイルはロックされています。読み取る前に一時的なコピーを作成する必要があります。

2. **プライバシー**: 閲覧履歴は機密情報を含む可能性があります。取り扱いには注意が必要です。

3. **複数プロファイル**: Chrome は複数のプロファイルをサポートしています。各プロファイルには独自の History ファイルがあります。
   - Default プロファイル: `~/Library/Application Support/Google/Chrome/Default/History`
   - その他: `~/Library/Application Support/Google/Chrome/Profile 1/History` など

## クエリ例

### 最新の訪問履歴を取得
```sql
SELECT
    datetime(visits.visit_time/1000000-11644473600, 'unixepoch', 'localtime') as visit_time,
    urls.url,
    urls.title
FROM visits
JOIN urls ON visits.url = urls.id
ORDER BY visits.visit_time DESC
LIMIT 100;
```

### ドメイン別の訪問回数
```sql
SELECT
    substr(url, instr(url, '://') + 3,
           instr(substr(url, instr(url, '://') + 3), '/') - 1) as domain,
    SUM(visit_count) as total_visits
FROM urls
GROUP BY domain
ORDER BY total_visits DESC
LIMIT 20;
```

### 滞在時間の長いページ
```sql
SELECT
    urls.title,
    urls.url,
    MAX(visits.visit_duration) / 1000000.0 as duration_seconds
FROM visits
JOIN urls ON visits.url = urls.id
WHERE visits.visit_duration > 0
GROUP BY urls.id
ORDER BY duration_seconds DESC
LIMIT 20;
```
