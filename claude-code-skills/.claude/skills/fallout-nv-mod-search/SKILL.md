---
name: fallout-nv-mod-search
description: Fallout New VegasのModをNexus Modsと日本語ブログ記事の両方から検索・分析するスキル。ユーザーが「Fallout New VegasのModを探して」「プレイヤーハウスのModを探して」「持ち運び可能なModを探して」などと依頼した際に使用する。Playwright MCPを活用したNexus Mods検索と、WebSearch/WebFetchによる日本語情報源の調査を統合し、総合的な評価を提供する。
---

# Fallout NV Mod Search

## Overview

Nexus ModsとWeb上の日本語情報源（ブログ、Wiki、レビューサイト）の**両方**からFallout New VegasのModを検索・分析し、ユーザーのニーズに合ったModを見つけるためのスキル。Playwright MCPツールを使用したNexus Modsのブラウジングと、WebSearch/WebFetchツールを使用した日本語情報収集を組み合わせ、海外と日本の両方の評価を統合した推奨を行う。

## 基本的なワークフロー

### 1. Nexus Modsへのアクセス

まず、Nexus ModsのFallout New Vegasページにアクセスする:

```
URL: https://www.nexusmods.com/newvegas/mods/categories/
```

`mcp__playwright__browser_navigate`ツールを使用してアクセスする。

### 2. カテゴリーの選択

ユーザーの要望に応じて適切なカテゴリーを選択する。主なカテゴリーは以下の通り（詳細は`references/categories.md`を参照）:

- **Player Homes** (803 files) - プレイヤーハウス
- **Weapons** (5,888 files) - 武器
- **Armour** (2,651 files) - 防具
- **Companions** (1,894 files) - コンパニオン
- **Gameplay Effects and Changes** (4,436 files) - ゲームプレイ変更
- **Quests and Adventures** (1,024 files) - クエスト・アドベンチャー
- **Models and Textures** (2,616 files) - モデル・テクスチャ
- **User Interfaces** (929 files) - UI
- **New Lands and Locations** (436 files) - 新しい土地・場所

カテゴリーリンクをクリックして、該当カテゴリーのModリストページに移動する。

### 3. フィルタリングと検索

必要に応じて以下のフィルターを適用する:

#### 検索パラメータ (Search parameters)
- **Title** - タイトルで検索
- **Description** - 説明文で検索
- **Author** - 作者で検索
- **Uploader** - アップローダーで検索

検索フィールドに入力後、「Apply」ボタンをクリックして適用する。

#### その他のフィルター
- **Language support** - 言語サポート
- **Content options** - コンテンツオプション（Vortexサポート、アダルトコンテンツなど）
- **File size** - ファイルサイズ範囲
- **Downloads** - ダウンロード数範囲
- **Endorsements** - 支持数範囲

### 4. ソート順の変更

Modリストを適切にソートして、最も関連性の高いModを見つける:

- **Date Published** - 公開日順（デフォルト）
- **Endorsements** - 支持数順（人気のModを探す場合に最適）
- **Downloads** - ダウンロード数順
- **Unique Downloads** - ユニークダウンロード数順
- **Last Updated** - 最終更新日順
- **Mod Name** - Mod名順
- **File Size** - ファイルサイズ順

「Sort by」ボタンをクリックして、適切なソート順を選択する。

### 5. 結果の分析と提示

検索結果から以下の情報を抽出してユーザーに提示する:

- **Mod名**
- **作者**
- **説明**
- **支持数 (Endorsements)**
- **ダウンロード数**
- **ファイルサイズ**
- **公開日/最終更新日**

特に人気のあるModや、ユーザーの要望に合致するModを強調して説明する。

### 6. 日本語情報源の調査（新規追加）

Nexus Modsでの検索結果を得た後、**必ず日本語の情報源も調査する**:

#### 6.1 WebSearchによる日本語記事検索

`WebSearch`ツールを使用して、以下のキーワードで日本語の情報を検索:

```
検索例:
- "Fallout New Vegas [カテゴリー名] mod おすすめ"
- "Fallout New Vegas [特定Mod名] レビュー 評価"
- "Fallout New Vegas mod 導入 [目的]"
```

主要な日本語情報源:
- **Game*Spark** (https://www.gamespark.jp) - ゲームニュース・Mod紹介
- **ゆるゲーマーメモ** (https://www.yurugamememo.com) - 詳細なModリスト
- **FalloutNewVegasWikiJP** (https://newvegas.fallout.z49.org) - 日本語Wiki
- **個人ブログ** - 実際のプレイ経験に基づくレビュー

#### 6.2 WebFetchによる詳細情報取得

見つかった日本語記事から、`WebFetch`ツールを使用して詳細情報を抽出:

```
プロンプト例:
- "この記事で推奨されているFallout New VegasのModについて、詳細情報を抽出してください"
- "このModの日本語レビューから、利点と欠点を抽出してください"
- "互換性や注意事項について記載されている内容を抽出してください"
```

#### 6.3 日本語情報からの重要ポイント

日本語情報源から以下の情報を特に確認:

- ✅ **実際の使用感** - 日本のユーザーの体験談
- ✅ **互換性問題** - 日本語環境での問題
- ✅ **推奨スペック** - 実際の動作報告
- ⚠️ **既知の不具合** - 日本語環境特有の問題
- 💡 **おすすめの組み合わせ** - 他のModとの相性
- 📝 **導入手順の注意点** - 日本語での解説

### 7. 総合評価と推奨

Nexus Modsの統計データと日本語情報源の評価を**統合**して、総合的な推奨を行う:

#### 評価基準

1. **Nexus Modsでの評価** (30%)
   - 支持数 (Endorsements)
   - ダウンロード数
   - コメント・レビュー

2. **日本語情報源での評価** (40%)
   - 日本のブログ/Wikiでの推奨度
   - 実際の使用報告
   - 既知の問題の有無

3. **技術的要素** (30%)
   - ファイルサイズ
   - 更新頻度
   - 互換性

#### 推奨フォーマット

```markdown
## 🏆 おすすめMod ランキング

### 🥇 1位: [Mod名]
- **Nexus評価:** [支持数] | [ダウンロード数]
- **日本での評価:** [日本語情報源からの評価]
- **特徴:** [主な機能]
- ⚠️ **注意点:** [日本語環境での問題があれば]
- 💡 **推奨理由:** [なぜおすすめか]

### 🥈 2位: [Mod名]
...
```

## 特定の要望への対応例

### 「持ち運び可能なMod」を探す場合

**ステップ1: Nexus Modsでの検索**
1. 適切なカテゴリー（例: Player Homes）を選択
2. Description検索で「portable」「mobile」「transportable」「summon」などのキーワードを試す
3. 人気順（Endorsements）でソートして上位を確認

**ステップ2: 日本語情報の確認**
1. `WebSearch`で「Fallout New Vegas 持ち運び mod プレイヤーハウス」を検索
2. 日本語Wikiやブログで推奨されているModを確認
3. 実際の使用感や互換性情報を収集

**ステップ3: 総合評価**
- Nexus Modsの統計と日本語レビューを統合
- 以下のような特徴を持つModを探す:
  - Mobile Truck Base - モバイルトラックベース
  - Vertibird Player Home - 召喚可能なVertibird
  - TTW - The USS Hoodwink - 移動可能な潜水艦

### 「グラフィック美化・4k対応Mod」を探す場合

**ステップ1: Nexus Modsでの検索**
1. Models and Texturesカテゴリーを選択
2. Description検索で「4k」「HD」「high resolution」を試す
3. 支持数順でソート

**ステップ2: 日本語情報の確認**（特に重要！）
1. `WebSearch`で「Fallout New Vegas 4k テクスチャ mod おすすめ HD」を検索
2. `WebFetch`でFalloutNewVegasWikiJP (https://newvegas.fallout.z49.org/?Mod%2F%E3%82%B0%E3%83%A9%E3%83%95%E3%82%A3%E3%83%83%E3%82%AF) から詳細情報取得
3. 日本語での評価を確認（例: 「調整不十分」「安定動作確認済み」などの重要情報）

**ステップ3: 統合評価の例**
```
🥇 NMC's Texture Pack
- Nexus評価: 高評価
- 日本での評価: 「定番Mod」「安定性が高い」
- 推奨理由: 実績と信頼性

🥈 Charge's FNV HD Texture Packs
- Nexus評価: 1,662支持、188k DL
- 日本での評価: 「包括性は高いがAI調整不十分」との指摘
- 注意: 日本のWikiでは細部の品質に課題あり
```

### 「共有ストレージ」を探す場合

**ステップ1: Nexus Modsでの検索**
1. Player HomesカテゴリーまたはUtilitiesカテゴリーを検索
2. Description検索で「shared storage」「linked containers」「connected storage」などを試す

**ステップ2: 日本語情報の確認**
1. `WebSearch`で「Fallout New Vegas ストレージ mod 共有」を検索
2. 日本語での代替案や組み合わせ方法を確認

**ステップ3: 推奨**
- 該当するModがない場合、人気のPlayer Home ModsやStash Organizerのようなストレージ管理Modを提案
- 日本語情報源から代替案を提示

## 使用するツール

このスキルでは以下のツールを使用する:

### Playwright MCPツール（Nexus Mods検索用）
- `mcp__playwright__browser_navigate` - ページへの移動
- `mcp__playwright__browser_snapshot` - ページの状態確認
- `mcp__playwright__browser_click` - 要素のクリック
- `mcp__playwright__browser_type` - テキストの入力
- `mcp__playwright__browser_wait_for` - ページの読み込み待機
- `mcp__playwright__browser_close` - ブラウザを閉じる

### Web検索ツール（日本語情報源調査用）
- `WebSearch` - 日本語のブログ記事、Wiki、レビューサイトを検索
- `WebFetch` - 見つかった記事から詳細情報を抽出

## 注意事項

### Nexus Mods検索
- 検索結果が0件の場合、キーワードを変更するか、カテゴリーを広げる
- 複数の候補がある場合、人気順や特徴的な機能でランク付けする
- Modの互換性やDLC要件などの重要情報があれば明記する

### 日本語情報源の活用
- **必ず日本語情報源も調査する** - Nexus Modsの統計だけでは不十分
- 日本語Wikiやブログでの評価を重視する（実際の使用経験に基づく）
- 日本語環境特有の問題や互換性情報を確認する
- 「定番Mod」「おすすめ」などの記載があれば重要視する
- ⚠️ 否定的な評価（「調整不十分」「不具合あり」など）も必ず報告する

### 総合評価
- Nexus Modsの統計（30%）と日本語情報源の評価（40%）を統合
- 日本語情報源での評価をより重視する（実際の使用経験が反映されているため）
- 矛盾がある場合（Nexusで高評価だが日本で低評価など）は必ず両方を明記
- 日本語での説明を心がけ、ユーザーにわかりやすく提示する

## Resources

### references/

カテゴリー情報や検索パラメータのリファレンスを含む。

### 日本語情報源リスト

#### 公式Wiki・データベース
- **FalloutNewVegasWikiJP** - https://newvegas.fallout.z49.org
  - Mod/グラフィック: https://newvegas.fallout.z49.org/?Mod%2F%E3%82%B0%E3%83%A9%E3%83%95%E3%82%A3%E3%83%83%E3%82%AF
  - 包括的なMod情報、日本語での詳細な解説

#### ニュース・レビューサイト
- **Game*Spark** - https://www.gamespark.jp
  - ゲームニュース、Mod紹介記事
  - 検索例: "site:gamespark.jp Fallout New Vegas mod"

#### 個人ブログ・攻略サイト
- **ゆるゲーマーメモ** - https://www.yurugamememo.com
  - 詳細なModリスト、導入手順
  - 実際のプレイ経験に基づくレビュー

- **あっさりゲーム計画** - https://assarigame.com
  - おすすめMod紹介
  - 初心者向け解説

- **Fallout4情報局** - https://fallout4.blog.jp
  - シリーズ全般のMod情報
  - 環境構築ガイド

#### コミュニティ・掲示板
- **Steam コミュニティ** - 日本語ディスカッション
- **個人ブログのコメント欄** - 実際のユーザー体験談

### 検索キーワード例

#### グラフィック系
```
- "Fallout New Vegas 4k テクスチャ mod おすすめ"
- "Fallout New Vegas グラフィック 美化 mod"
- "Fallout New Vegas ENB おすすめ"
- "Fallout New Vegas NMC テクスチャ"
```

#### ゲームプレイ系
```
- "Fallout New Vegas mod 導入 おすすめ"
- "Fallout New Vegas 武器 mod"
- "Fallout New Vegas クエスト mod"
- "Fallout New Vegas コンパニオン mod"
```

#### 問題解決系
```
- "Fallout New Vegas mod 互換性"
- "Fallout New Vegas mod エラー 対処"
- "Fallout New Vegas mod ロードオーダー"
```

## ワークフロー図

```
ユーザーリクエスト
    ↓
┌─────────────────────────────────────┐
│ 1. Nexus Modsで検索                │
│   - カテゴリー選択                  │
│   - キーワード検索                  │
│   - ソート（人気順）                │
│   - トップ10-20を確認               │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ 2. 日本語情報源で調査（並行）       │
│   - WebSearch で記事検索            │
│   - WebFetch で詳細取得             │
│   - Wiki/ブログの評価確認           │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ 3. 情報を統合                       │
│   - Nexus統計: 30%                  │
│   - 日本語評価: 40%                 │
│   - 技術要素: 30%                   │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│ 4. ランキング形式で推奨             │
│   - 🥇🥈🥉 形式                      │
│   - 両方の評価を明記                │
│   - 注意点・互換性情報              │
└─────────────────────────────────────┘
    ↓
ユーザーへの総合的な推奨
```
