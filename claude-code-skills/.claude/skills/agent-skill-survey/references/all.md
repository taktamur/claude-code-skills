# Agent Skills リファレンス一覧

SQLiteデータベースから自動生成。

- **総件数**: 164件
- **日本語**: 40件
- **英語**: 124件
- **最終更新**: 2025-12-30

---

## SkillPort - Agent Skills運用管理ツール

- **日付**: 調査日 2025-12-30
- **URL**: https://github.com/gotalab/skillport
- **タグ**: cross-platform, mcp, skillops
- **要約**:
  - Agent Skillsの検証、管理、配信を行うSkillOpsツールキット
  - CLI/MCP経由で複数のエージェント（Cursor、Windsurf、Cline等）にスキルを提供
  - GitHubやローカルパスからのスキルインストール・更新・削除機能
  - 検索優先パターンで軽量配信（メタデータ約100トークン、必要時に完全指示ロード）

---

## The Security Gap in AI Agent Ecosystems: A Deep Dive into Static Analysis for Claude Skills

- **日付**: 2025-12-29
- **URL**: https://dev.to/beck_moulton/the-security-gap-in-ai-agent-ecosystems-a-deep-dive-into-static-analysis-for-claude-skills-5cbk
- **要約**:
  - Skillsインストール時の開発環境への広範なアクセス権付与によるセキュリティリスクを指摘
  - 認証情報窃取やマルウェア注入のリスクを警告
  - Skill-Security-Scannerという静的分析ツールで5領域のリスク評価を提案

---

## 【Claude Code】Agent SkillsとMCPの違いを徹底解説 - 補完関係を理解して使いこなす

- **日付**: 2025-12-29
- **URL**: https://qiita.com/masayan1126/items/20fa457b8ba6994b6d0d
- **要約**:
  - Agent Skillsはファイルシステムベースの「手続き的知識」を集約
  - MCPと比べてトークン消費量が少なく、メンテナンスが容易
  - 「MCPで素材を集め、Skillsで料理する」という役割分担を提唱

---

## 発表から約2週間、いますぐ使えるAgent Skills 10選

- **日付**: 2025-12-28
- **URL**: https://note.com/timakin/n/na8b2789897ea
- **要約**:
  - Agent Skills発表後わずか数日でOpenAIとGitHub Copilotが採用し業界標準化が進行
  - ドキュメント処理系、開発ワークフロー系、エンタープライズ連携系を紹介
  - MCPと比べてサーバー不要で扱いやすいポータビリティとシンプルさが利点

---

## 【非エンジニア必見】会話だけで"自分専用AI"を作る！Claude Code「Agent Skills」完全入門

- **日付**: 2025-12-27
- **URL**: https://note.com/renkon40/n/n6d17f9098cfb
- **要約**:
  - 仕事の手順をAIに体に叩き込ませる機能としてのAgent Skills
  - Skill Creatorツールを使用し会話形式だけでコードレビュースキルを構築
  - プロンプトとプログラムの両方を組み合わせられるハイブリッドアプローチ

---

## Claude Agent Skills: Teaching Your AI Agent to Wear Multiple Hats

- **日付**: 2025-12-26
- **URL**: https://dev.to/cloudnative_eng/claude-agent-skills-teaching-your-ai-agent-to-wear-multiple-hats-2o11
- **要約**:
  - プログレッシブコンテキストローディングで必要な時だけ関連情報を読み込む
  - スキルはSKILL.mdファイルを含むフォルダで、特別なセットアップ不要
  - 複数プロジェクト間での再利用性とシンプルな構造が特徴

---

## Claude Codeアドベントカレンダー: 24 Tipsまとめ

- **日付**: 2025-12-26
- **URL**: https://zenn.dev/oikon/articles/cc-advent-calendar
- **要約**:
  - skill-creatorを使用してAgent Skillsを簡単に作成する方法を紹介
  - ベストプラクティス: SKILL.mdは500行以下、例は具体的に、ファイル参照は深さ1階層まで
  - GitHub Actions環境でAgent Skillsを活用しCI/CDパイプライン内で専門タスク実行

---

## How I Built an Autonomous AI Startup System with 37 Agents Using Claude Code

- **日付**: 2025-12-26
- **URL**: https://dev.to/asklokesh/how-i-built-an-autonomous-ai-startup-system-with-37-agents-using-claude-code-2p79
- **要約**:
  - Loki Modeオープンソースskillで37専門エージェントをオーケストレーション
  - Engineering、Operations、Business、Data、Product、Growth、Reviewの機能別スウォーム
  - 並列コードレビュー、circuit breaker、dead letter queue、state persistenceを実装

---

## Agent Skills(Claude Skills)とは？作成手順や使い方、料金を徹底解説！

- **日付**: 調査日 2025-12-25
- **URL**: https://www.ai-souken.com/article/what-is-agent-skills-claude
- **タグ**: tutorial
- **要約**:
  - AI総合研究所によるAgent Skills解説。作成手順、YAML構造、Pro/Max/Team/Enterprise対応。社内FAQ自動応答化、定型業務自動化などの活用例。追加料金なし。

---

## Agent Skillsに全部賭ける価値はあるか

- **日付**: 調査日 2025-12-25
- **URL**: https://zenn.dev/tkithrta/articles/f07b7b8cdb7d0c
- **タグ**: open-standard
- **要約**:
  - Agent Skillsはファイルシステムベースとツールベースの両方で実装可能
  - name最大64文字、description最大1024文字でコンテキストエンジニアリング問題を解決
  - AGENTS.mdの欠点（ファイル名の曖昧さ、Frontmatter非対応など）を克服
  - スキルの親ディレクトリが仕様に含まれていない点が唯一の課題

---

## Agent Skills徹底解説！Claudeが【スキルを覚えるAI】へ進化！業務知識を丸ごと学習できる新時代へ

- **日付**: 調査日 2025-12-25
- **URL**: https://weel.co.jp/media/innovator/agent-skills/
- **タグ**: tutorial
- **要約**:
  - WEEL社によるAgent Skills解説。業務知識パッケージ化の概念、チーム全体での品質統一、定型業務自動化のユースケース紹介。

---

## Brand Guidelines - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/brand-guidelines
- **タグ**: business, curated-list
- **要約**:
  - Applies Anthropic's official brand colors and typography to artifacts for consistent visual identity and professional design standards.
  - カテゴリ: business
  - ソース: awesome-claude-skills

---

## CSV Data Summarizer - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/coffeefuelbump/csv-data-summarizer-claude-skill
- **タグ**: curated-list, data-analysis
- **要約**:
  - Automatically analyzes CSV files and generates comprehensive insights with visualizations without requiring user prompts.
  - カテゴリ: data-analysis
  - ソース: awesome-claude-skills

---

## Canvas Design - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/canvas-design
- **タグ**: creative, curated-list
- **要約**:
  - Creates beautiful visual art in PNG and PDF documents using design philosophy and aesthetic principles for posters, designs, and static pieces.
  - カテゴリ: creative
  - ソース: awesome-claude-skills

---

## Changelog Generator - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/changelog-generator
- **タグ**: curated-list, dev-tools
- **要約**:
  - Automatically creates user-facing changelogs from git commits by analyzing history and transforming technical commits into customer-friendly release notes.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## Claude Code Terminal Title - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/bluzername/claude-code-terminal-title
- **タグ**: curated-list, dev-tools
- **要約**:
  - Gives each Claude-Code terminal window a dynamic title that describes the work being done.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## Claude Code の Agent Skills って？

- **日付**: 調査日 2025-12-25
- **URL**: https://zenn.dev/rudy/articles/291354cfb4ef801d976ee593c942f543
- **要約**:
  - Agent Skills基礎解説。.claude/skills/ディレクトリ構造、Claudeによる自動判断と知識活用の仕組みを説明。

---

## Claude Skillsとは？ AIエージェント開発における新たなベストプラクティスをやさしく解説

- **日付**: 調査日 2025-12-25
- **URL**: https://codezine.jp/article/detail/22677
- **タグ**: comparison
- **要約**:
  - Claude Skills解説記事。CLAUDE.md/MCP/Subagentsとの違いを明確化。Metadataのみ初期読み込みでコンテキスト効率化。ドメイン知識増加によるエージェント増殖問題を解決。

---

## Claude codeでリポジトリにあったAgent Skillsを一発で作成するコマンドを作った

- **日付**: 調査日 2025-12-25
- **URL**: https://zenn.dev/tesla/articles/88f05514be851d
- **要約**:
  - /repo-initコマンドでリポジトリ情報から自動的にAgent Skillsを生成
  - 「手順書の塊」としてSkillsを捉える視点を提示
  - 関連Subagentも同時に生成される仕組み
  - 改行がスキル読み込みを阻害する問題など実装上の課題も報告

---

## Competitive Ads Extractor - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/competitive-ads-extractor
- **タグ**: business, curated-list
- **要約**:
  - Extracts and analyzes competitors' ads from ad libraries to understand messaging and creative approaches that resonate.
  - カテゴリ: business
  - ソース: awesome-claude-skills

---

## Content Research Writer - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/content-research-writer
- **タグ**: curated-list, writing
- **要約**:
  - Assists in writing high-quality content by conducting research, adding citations, improving hooks, and providing section-by-section feedback.
  - カテゴリ: writing
  - ソース: awesome-claude-skills

---

## D3.js Visualization - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/chrisvoncsefalvay/claude-d3js-skill
- **タグ**: curated-list, dev-tools
- **要約**:
  - Teaches Claude to produce D3 charts and interactive data visualizations.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## Domain Name Brainstormer - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/domain-name-brainstormer
- **タグ**: business, curated-list
- **要約**:
  - Generates creative domain name ideas and checks availability across multiple TLDs including .com, .io, .dev, and .ai extensions.
  - カテゴリ: business
  - ソース: awesome-claude-skills

---

## FFUF Web Fuzzing - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/jthack/ffuf_claude_skill
- **タグ**: curated-list, dev-tools
- **要約**:
  - Integrates the ffuf web fuzzer so Claude can run fuzzing tasks and analyze results for vulnerabilities.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## File Organizer - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/file-organizer
- **タグ**: curated-list, productivity
- **要約**:
  - Intelligently organizes files and folders by understanding context, finding duplicates, and suggesting better organizational structures.
  - カテゴリ: productivity
  - ソース: awesome-claude-skills

---

## Image Enhancer - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/image-enhancer
- **タグ**: creative, curated-list
- **要約**:
  - Improves image and screenshot quality by enhancing resolution, sharpness, and clarity for professional presentations and documentation.
  - カテゴリ: creative
  - ソース: awesome-claude-skills

---

## Internal Comms - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/internal-comms
- **タグ**: business, curated-list
- **要約**:
  - Helps write internal communications including 3P updates, company newsletters, FAQs, status reports, and project updates using company-specific formats.
  - カテゴリ: business
  - ソース: awesome-claude-skills

---

## Invoice Organizer - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/invoice-organizer
- **タグ**: curated-list, productivity
- **要約**:
  - Automatically organizes invoices and receipts for tax preparation by reading files, extracting information, and renaming consistently.
  - カテゴリ: productivity
  - ソース: awesome-claude-skills

---

## K-Dense-AI/claude-scientific-skills

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/K-Dense-AI/claude-scientific-skills
- **タグ**: curated-list, scientific
- **要約**:
  - 125+の科学研究向けスキル集。生物情報学、化学情報学、臨床研究、ML、医療画像処理など15+分野をカバー。26+のデータベース、54+のPythonパッケージ統合。2.3k Star。

---

## Lead Research Assistant - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/lead-research-assistant
- **タグ**: business, curated-list
- **要約**:
  - Identifies and qualifies high-quality leads by analyzing your product, searching for target companies, and providing actionable outreach strategies.
  - カテゴリ: business
  - ソース: awesome-claude-skills

---

## MCP Builder - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/mcp-builder
- **タグ**: curated-list, dev-tools
- **要約**:
  - Guides creation of high-quality MCP (Model Context Protocol) servers for integrating external APIs and services with LLMs using Python or TypeScript.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## Markdown to EPUB Converter - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/smerchek/claude-epub-skill
- **タグ**: curated-list, document-processing
- **要約**:
  - Converts markdown documents and chat summaries into professional EPUB ebook files.
  - カテゴリ: document-processing
  - ソース: awesome-claude-skills

---

## Meeting Insights Analyzer - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/meeting-insights-analyzer
- **タグ**: curated-list, writing
- **要約**:
  - Analyzes meeting transcripts to uncover behavioral patterns including conflict avoidance, speaking ratios, filler words, and leadership style.
  - カテゴリ: writing
  - ソース: awesome-claude-skills

---

## NotebookLM Integration - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/PleasePrompto/notebooklm-skill
- **タグ**: curated-list, writing
- **要約**:
  - Lets Claude Code chat directly with NotebookLM for source-grounded answers based exclusively on uploaded documents.
  - カテゴリ: writing
  - ソース: awesome-claude-skills

---

## Notion Skills for Claude

- **日付**: 調査日 2025-12-25
- **URL**: https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0
- **タグ**: curated-list, productivity
- **要約**:
  - Skills for working with Notion.
  - カテゴリ: productivity
  - ソース: VoltAgent/awesome-claude-skills

---

## Playwright Browser Automation - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/lackeyjb/playwright-skill
- **タグ**: curated-list, dev-tools
- **要約**:
  - Model-invoked Playwright automation for testing and validating web applications.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## Raffle Winner Picker - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/raffle-winner-picker
- **タグ**: curated-list, productivity
- **要約**:
  - Randomly selects winners from lists, spreadsheets, or Google Sheets for giveaways and contests with cryptographically secure randomness.
  - カテゴリ: productivity
  - ソース: awesome-claude-skills

---

## Skill Creator - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/skill-creator
- **タグ**: curated-list, dev-tools
- **要約**:
  - Provides guidance for creating effective Claude Skills that extend capabilities with specialized knowledge, workflows, and tool integrations.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## Skill Seekers - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/yusufkaraaslan/Skill_Seekers
- **タグ**: curated-list, dev-tools
- **要約**:
  - Automatically converts any documentation website into a Claude AI skill in minutes.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## Skills explained: How Skills compares to prompts, Projects, MCP, and subagents

- **日付**: 調査日 2025-12-25
- **URL**: https://claude.com/blog/skills-explained
- **タグ**: comparison, mcp, official
- **要約**:
  - Skills vs 他機能の比較：Prompts（一時的指示）、Projects（ワークスペース）、MCP（外部接続）、Subagents（特化AI）
  - Projectsは「何を知っているか」、Skillsは「何ができるか」を定義
  - 競争分析エージェント例：Projects + MCP + Skills + Subagentsの組み合わせ
  - スキルは専門知識を教えるツールで、必要に応じて動的に読み込み

---

## SkillsMP - Agent Skills Marketplace

- **日付**: 調査日 2025-12-25
- **URL**: https://skillsmp.com
- **タグ**: open-standard
- **要約**:
  - Claude、Codex、ChatGPT向けのスキルマーケットプレイス
  - 2025年12月のオープンスタンダード化に対応
  - 複数AIツール間でスキルを共有可能

---

## Slack GIF Creator - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/slack-gif-creator
- **タグ**: creative, curated-list
- **要約**:
  - Creates animated GIFs optimized for Slack with validators for size constraints and composable animation primitives.
  - カテゴリ: creative
  - ソース: awesome-claude-skills

---

## Theme Factory - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/theme-factory
- **タグ**: creative, curated-list
- **要約**:
  - Applies professional font and color themes to artifacts including slides, docs, reports, and HTML landing pages with 10 pre-set themes.
  - カテゴリ: creative
  - ソース: awesome-claude-skills

---

## Video Downloader - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/video-downloader
- **タグ**: creative, curated-list
- **要約**:
  - Downloads videos from YouTube and other platforms for offline viewing, editing, or archival with support for various formats and quality options.
  - カテゴリ: creative
  - ソース: awesome-claude-skills

---

## VoltAgent/awesome-claude-skills

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/VoltAgent/awesome-claude-skills
- **タグ**: curated-list, dev-tools, git-workflow
- **要約**:
  - VoltAgentコミュニティによるClaude Skillsキュレーションリスト
  - Git/GitHub workflow skills: git-commit、github-pr-creation/merge/review
  - obra/superpowers: TDD、デバッグ、コラボレーションパターンを含む20+のスキル
  - カテゴリ別整理：生産性、開発テスト、専門ドメイン
  - スキル作成ガイドも含む

---

## Webapp Testing - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills/blob/master/webapp-testing
- **タグ**: curated-list, dev-tools
- **要約**:
  - Tests local web applications using Playwright for verifying frontend functionality, debugging UI behavior, and capturing screenshots.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## article-extractor - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/article-extractor
- **タグ**: curated-list, writing
- **要約**:
  - Extract full article text and metadata from web pages.
  - カテゴリ: writing
  - ソース: awesome-claude-skills

---

## artifacts-builder - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/anthropics/skills/tree/main/web-artifacts-builder
- **タグ**: curated-list, dev-tools
- **要約**:
  - Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui).
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## aws-skills - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/zxkane/aws-skills
- **タグ**: curated-list, dev-tools
- **要約**:
  - AWS development with CDK best practices, cost optimization MCP servers, and serverless/event-driven architecture patterns.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## brainstorming - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/tree/main/skills/brainstorming
- **タグ**: curated-list, writing
- **要約**:
  - Transform rough ideas into fully-formed designs through structured questioning and alternative exploration.
  - カテゴリ: writing
  - ソース: awesome-claude-skills

---

## claude-win11-speckit-update-skill - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/NotMyself/claude-win11-speckit-update-skill
- **タグ**: curated-list, productivity
- **要約**:
  - Windows 11 system management.
  - カテゴリ: productivity
  - ソース: VoltAgent/awesome-claude-skills

---

## claudisms - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/jeffersonwarrior/claudisms
- **タグ**: curated-list, productivity
- **要約**:
  - SMS messaging integration.
  - カテゴリ: productivity
  - ソース: VoltAgent/awesome-claude-skills

---

## commands - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/tree/main/skills/commands
- **タグ**: curated-list, dev-tools
- **要約**:
  - Create and manage command structures.
  - カテゴリ: dev-tools
  - ソース: VoltAgent/awesome-claude-skills

---

## computer-forensics - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/computer-forensics
- **タグ**: curated-list, security
- **要約**:
  - Digital forensics analysis and investigation techniques.
  - カテゴリ: security
  - ソース: awesome-claude-skills

---

## condition-based-waiting - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/condition-based-waiting/SKILL.md
- **タグ**: curated-list, dev-tools
- **要約**:
  - Manage conditional pauses or delays.
  - カテゴリ: dev-tools
  - ソース: VoltAgent/awesome-claude-skills

---

## defense-in-depth - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/defense-in-depth/SKILL.md
- **タグ**: curated-list, security
- **要約**:
  - Multi-layered security approaches.
  - カテゴリ: security
  - ソース: VoltAgent/awesome-claude-skills

---

## dev-agent-skills - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/fvadicamo/dev-agent-skills
- **タグ**: curated-list, dev-tools, git-workflow
- **要約**:
  - Git and GitHub workflow skills: git-commit (Conventional Commits), github-pr-creation, github-pr-merge, github-pr-review, plus creating-skills guide.
  - カテゴリ: dev-tools
  - ソース: VoltAgent/awesome-claude-skills

---

## dispatching-parallel-agents - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/dispatching-parallel-agents/SKILL.md
- **タグ**: curated-list, dev-tools, subagent
- **要約**:
  - Coordinate multiple simultaneous agents.
  - カテゴリ: dev-tools
  - ソース: VoltAgent/awesome-claude-skills

---

## docx - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/anthropics/skills/tree/main/document-skills/docx
- **タグ**: curated-list, document-processing
- **要約**:
  - Create, edit, analyze Word docs with tracked changes, comments, formatting.
  - カテゴリ: document-processing
  - ソース: awesome-claude-skills

---

## executing-plans - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/executing-plans/SKILL.md
- **タグ**: curated-list, productivity
- **要約**:
  - Implement and run strategic plans.
  - カテゴリ: productivity
  - ソース: VoltAgent/awesome-claude-skills

---

## family-history-research - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/emaynard/claude-family-history-research-skill
- **タグ**: curated-list, writing
- **要約**:
  - Provides assistance with planning family history and genealogy research projects.
  - カテゴリ: writing
  - ソース: awesome-claude-skills

---

## file-deletion - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/file-deletion
- **タグ**: curated-list, security
- **要約**:
  - Secure file deletion and data sanitization methods.
  - カテゴリ: security
  - ソース: awesome-claude-skills

---

## finishing-a-development-branch - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/tree/main/skills/finishing-a-development-branch
- **タグ**: curated-list, dev-tools
- **要約**:
  - Guides completion of development work by presenting clear options and handling chosen workflow.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## git-pushing - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/git-pushing
- **タグ**: collaboration, curated-list
- **要約**:
  - Automate git operations and repository interactions.
  - カテゴリ: collaboration
  - ソース: awesome-claude-skills

---

## iOS Simulator - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/conorluddy/ios-simulator-skill
- **タグ**: curated-list, dev-tools
- **要約**:
  - Enables Claude to interact with iOS Simulator for testing and debugging iOS applications.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## imagen - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/sanjay3290/ai-skills/tree/main/skills/imagen
- **タグ**: creative, curated-list
- **要約**:
  - Generate images using Google Gemini's API for UI mockups, icons, and visual assets.
  - カテゴリ: creative
  - ソース: VoltAgent/awesome-claude-skills

---

## kaizen - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/kaizen/skills/kaizen
- **タグ**: curated-list, productivity
- **要約**:
  - Applies continuous improvement methodology with multiple analytical approaches, based on Japanese Kaizen philosophy and Lean methodology.
  - カテゴリ: productivity
  - ソース: awesome-claude-skills

---

## levnikolaevich/claude-code-skills

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/levnikolaevich/claude-code-skills
- **タグ**: agile, curated-list, linear
- **要約**:
  - 52のAgileワークフロー自動化スキル。Linear MCP統合でEpic→ストーリー→タスク実行まで一貫管理。ドキュメント、計画、実行、品質、監査の6カテゴリ。

---

## linear-claude-skill - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/wrsmith108/linear-claude-skill
- **タグ**: curated-list, mcp, productivity
- **要約**:
  - Manage Linear issues, projects, and teams with MCP tools, SDK scripts, and GraphQL fallbacks.
  - カテゴリ: productivity
  - ソース: VoltAgent/awesome-claude-skills

---

## materials-simulation-skills - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/HeshamFS/materials-simulation-skills
- **タグ**: curated-list, data-analysis
- **要約**:
  - Agent skills for computational materials science: numerical stability, time-stepping, linear solvers, mesh generation, simulation validation, parameter optimization, and post-processing.
  - カテゴリ: data-analysis
  - ソース: VoltAgent/awesome-claude-skills

---

## metadata-extraction - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/mhattingpete/claude-skills-marketplace/tree/main/computer-forensics-skills/skills/metadata-extraction
- **タグ**: curated-list, security
- **要約**:
  - Extract and analyze file metadata for forensic purposes.
  - カテゴリ: security
  - ソース: awesome-claude-skills

---

## move-code-quality-skill - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/1NickPappas/move-code-quality-skill
- **タグ**: curated-list, dev-tools
- **要約**:
  - Analyzes Move language packages against the official Move Book Code Quality Checklist for Move 2024 Edition compliance and best practices.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## n8n-skills - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/haunchen/n8n-skills
- **タグ**: curated-list, productivity
- **要約**:
  - Enables AI assistants to directly understand and operate n8n workflows.
  - カテゴリ: productivity
  - ソース: awesome-claude-skills

---

## obra/superpowers

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers
- **タグ**: tdd
- **要約**:
  - Claude Code用のバトルテスト済みスキルライブラリ
  - 20+のスキル：TDD、デバッグ、コラボレーションパターン
  - brainstorming、writing-plans、executing-plans
  - test-driven-development、systematic-debugging、root-cause-tracing
  - dispatching-parallel-agents、verification-before-completion

---

## pdf - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/anthropics/skills/tree/main/document-skills/pdf
- **タグ**: curated-list, document-processing
- **要約**:
  - Extract text, tables, metadata, merge & annotate PDFs.
  - カテゴリ: document-processing
  - ソース: awesome-claude-skills

---

## postgres - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/sanjay3290/ai-skills/tree/main/skills/postgres
- **タグ**: curated-list, data-analysis
- **要約**:
  - Execute safe read-only SQL queries against PostgreSQL databases with multi-connection support.
  - カテゴリ: data-analysis
  - ソース: VoltAgent/awesome-claude-skills

---

## pptx - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/anthropics/skills/tree/main/document-skills/pptx
- **タグ**: curated-list, document-processing
- **要約**:
  - Read, generate, and adjust slides, layouts, templates.
  - カテゴリ: document-processing
  - ソース: awesome-claude-skills

---

## prompt-engineering - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/customaize-agent/skills/prompt-engineering
- **タグ**: curated-list, dev-tools
- **要約**:
  - Teaches well-known prompt engineering techniques and patterns, including Anthropic best practices and agent persuasion principles.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## pypict-claude-skill - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/omkamal/pypict-claude-skill
- **タグ**: curated-list, dev-tools
- **要約**:
  - Design comprehensive test cases using PICT (Pairwise Independent Combinatorial Testing) for requirements or code, generating optimized test suites with pairwise coverage.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## receiving-code-review - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/receiving-code-review/SKILL.md
- **タグ**: collaboration, curated-list
- **要約**:
  - Process and incorporate code feedback.
  - カテゴリ: collaboration
  - ソース: VoltAgent/awesome-claude-skills

---

## requesting-code-review - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md
- **タグ**: collaboration, curated-list
- **要約**:
  - Initiate code review processes.
  - カテゴリ: collaboration
  - ソース: VoltAgent/awesome-claude-skills

---

## review-implementing - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/review-implementing
- **タグ**: collaboration, curated-list
- **要約**:
  - Evaluate code implementation plans and align with specs.
  - カテゴリ: collaboration
  - ソース: awesome-claude-skills

---

## root-cause-tracing - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/tree/main/skills/root-cause-tracing
- **タグ**: curated-list, data-analysis
- **要約**:
  - Use when errors occur deep in execution and you need to trace back to find the original trigger.
  - カテゴリ: data-analysis
  - ソース: awesome-claude-skills

---

## security-bluebook-builder - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/SHADOWPR0/security-bluebook-builder
- **タグ**: curated-list, security
- **要約**:
  - Build a concise, normative security Blue Book for sensitive apps (threat model, data classes, auth/session, logging/audit, retention, IR, security gates).
  - カテゴリ: security
  - ソース: VoltAgent/awesome-claude-skills

---

## sharing-skills - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/sharing-skills/SKILL.md
- **タグ**: curated-list, dev-tools
- **要約**:
  - Distribute and communicate capabilities.
  - カテゴリ: dev-tools
  - ソース: VoltAgent/awesome-claude-skills

---

## ship-learn-next - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/ship-learn-next
- **タグ**: curated-list, productivity
- **要約**:
  - Skill to help iterate on what to build or learn next, based on feedback loops.
  - カテゴリ: productivity
  - ソース: awesome-claude-skills

---

## software-architecture - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/ddd/skills/software-architecture
- **タグ**: curated-list, dev-tools
- **要約**:
  - Implements design patterns including Clean Architecture, SOLID principles, and comprehensive software design best practices.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## subagent-driven-development - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/NeoLabHQ/context-engineering-kit/tree/master/plugins/sadd/skills/subagent-driven-development
- **タグ**: curated-list, dev-tools
- **要約**:
  - Dispatches independent subagents for individual tasks with code review checkpoints between iterations for rapid, controlled development.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## superpowers-lab - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers-lab
- **タグ**: curated-list, dev-tools
- **要約**:
  - Experimental skills for Claude Code Superpowers.
  - Uses new techniques that are still being refined and tested.
  - カテゴリ: dev-tools
  - ソース: VoltAgent/awesome-claude-skills

---

## systematic-debugging - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md
- **タグ**: curated-list, dev-tools
- **要約**:
  - Methodical problem-solving in code.
  - カテゴリ: dev-tools
  - ソース: VoltAgent/awesome-claude-skills

---

## tapestry - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/tapestry
- **タグ**: curated-list, productivity
- **要約**:
  - Interlink and summarize related documents into knowledge networks.
  - カテゴリ: productivity
  - ソース: awesome-claude-skills

---

## test-driven-development - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/tree/main/skills/test-driven-development
- **タグ**: curated-list, dev-tools
- **要約**:
  - Use when implementing any feature or bugfix, before writing implementation code.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## test-fixing - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/mhattingpete/claude-skills-marketplace/tree/main/engineering-workflow-plugin/skills/test-fixing
- **タグ**: collaboration, curated-list
- **要約**:
  - Detect failing tests and propose patches or fixes.
  - カテゴリ: collaboration
  - ソース: awesome-claude-skills

---

## testing-anti-patterns - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/testing-anti-patterns/SKILL.md
- **タグ**: curated-list, dev-tools
- **要約**:
  - Identify ineffective testing practices.
  - カテゴリ: dev-tools
  - ソース: VoltAgent/awesome-claude-skills

---

## testing-skills-with-subagents - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/testing-skills-with-subagents/SKILL.md
- **タグ**: curated-list, dev-tools, subagent
- **要約**:
  - Collaborative testing approaches using subagents.
  - カテゴリ: dev-tools
  - ソース: VoltAgent/awesome-claude-skills

---

## threat-hunting-with-sigma-rules - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/jthack/threat-hunting-with-sigma-rules-skill
- **タグ**: curated-list, security
- **要約**:
  - Use Sigma detection rules to hunt for threats and analyze security events.
  - カテゴリ: security
  - ソース: awesome-claude-skills

---

## using-git-worktrees - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/using-git-worktrees/
- **タグ**: curated-list, dev-tools
- **要約**:
  - Creates isolated git worktrees with smart directory selection and safety verification.
  - カテゴリ: dev-tools
  - ソース: awesome-claude-skills

---

## using-superpowers - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/using-superpowers/SKILL.md
- **タグ**: curated-list, dev-tools
- **要約**:
  - Leverage core platform capabilities.
  - カテゴリ: dev-tools
  - ソース: VoltAgent/awesome-claude-skills

---

## varlock-claude-skill - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/wrsmith108/varlock-claude-skill
- **タグ**: curated-list, security
- **要約**:
  - Secure environment variable management ensuring secrets are never exposed in Claude sessions, terminals, logs, or git commits.
  - カテゴリ: security
  - ソース: VoltAgent/awesome-claude-skills

---

## verification-before-completion - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md
- **タグ**: curated-list, dev-tools
- **要約**:
  - Validate work before finalizing.
  - カテゴリ: dev-tools
  - ソース: VoltAgent/awesome-claude-skills

---

## vexor - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/scarletkc/vexor
- **タグ**: curated-list, dev-tools
- **要約**:
  - Vector-powered CLI for semantic file search with Claude/Codex skill.
  - カテゴリ: dev-tools
  - ソース: VoltAgent/awesome-claude-skills

---

## web-asset-generator - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/alonw0/web-asset-generator
- **タグ**: creative, curated-list
- **要約**:
  - Generates web assets like favicons, app icons, and social media images.
  - カテゴリ: creative
  - ソース: travisvn/awesome-claude-skills

---

## writing-plans - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md
- **タグ**: curated-list, productivity
- **要約**:
  - Create strategic documentation and plans.
  - カテゴリ: productivity
  - ソース: VoltAgent/awesome-claude-skills

---

## writing-skills - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md
- **タグ**: curated-list, dev-tools, skill-creator
- **要約**:
  - Develop and document capabilities.
  - カテゴリ: dev-tools
  - ソース: VoltAgent/awesome-claude-skills

---

## xlsx - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/anthropics/skills/tree/main/document-skills/xlsx
- **タグ**: curated-list, document-processing
- **要約**:
  - Spreadsheet manipulation: formulas, charts, data transformations.
  - カテゴリ: document-processing
  - ソース: awesome-claude-skills

---

## youtube-transcript - Claude Skill

- **日付**: 調査日 2025-12-25
- **URL**: https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/youtube-transcript
- **タグ**: creative, curated-list
- **要約**:
  - Fetch transcripts from YouTube videos and prepare summaries.
  - カテゴリ: creative
  - ソース: awesome-claude-skills

---

## Agent Skillsの作り方とベストプラクティス 徹底解説

- **日付**: 2025-12-24
- **URL**: https://note.com/masa_wunder/n/nffa03e1d5999
- **要約**:
  - Claude Code、OpenAI Codex、Cursor、VS Code GitHub Copilotなど主要プラットフォームで採用
  - 段階的情報開示で10個インストール時に約1,000トークンのベースラインを実現
  - ディレクトリ構造、YAMLメタデータ、配布方法、セキュリティ考慮事項を網羅

---

## ClaudeのAgent Skillsがオープン標準になったらしいので、Github Copilotで検証してみた

- **日付**: 2025-12-24
- **URL**: https://qiita.com/shachidaikon/items/dad20f837e7fb923761d
- **要約**:
  - Agent Skillsがオープンスタンダードとして公開され他ツールでも利用可能に
  - Claude向けのSkillをGitHub Copilotで直接使用できることを検証
  - AIツールが変わる度の初期セットアップ手間を削減できる利点

---

## 🔥 はじめての Agent Skills 🔥 12 選＆リポジトリ一覧！GitHub Copilot でも使える AI の手順書

- **日付**: 2025-12-24
- **URL**: https://qiita.com/aktsmm/items/08eef2cdeeb0a32b69a2
- **要約**:
  - Agent SkillsがAnthropicによりオープンスタンダード化（2025-12-19）
  - GitHub Copilot、VS Code、Cursorなど複数プラットフォームで利用可能
  - 文書作成、テスト自動化、開発ワークフロー最適化など12選を紹介

---

## Claude Code Skillsの作り方｜自作 vs Skill Creator

- **日付**: 2025-12-23
- **URL**: https://qiita.com/iwashiMadai/items/2b2c7294d308a4d1f9b3
- **要約**:
  - Skillの選択はYAML frontmatterのnameとdescriptionフィールドのみに基づく
  - 三人称での記述、「Use when...」構文、具体的キーワードがベストプラクティス
  - 自作Skillとskill-creator生成版の比較でベストプラクティスの重要性を実証

---

## 【決定版】Agent Skillsがオープン標準に！Claude、Cursor、GitHubで使い回せる時代へ

- **日付**: 2025-12-22
- **URL**: https://note.com/yasuda_forceai/n/nb88b61f00d6d
- **要約**:
  - Agent Skillsがオープン標準化され複数プラットフォームで使い回し可能に
  - 段階的開示によるトークン効率化、SKILL.mdの書き方、自由度設定を解説
  - ワークフロー効率90%削減、コードレビュー時間60%削減の成果を報告

---

## Claudeをあなた専用のアシスタントに育てる「agent skills」入門

- **日付**: 2025-12-21
- **URL**: https://zenn.dev/shintaroamaike/articles/f14eb0562e93e7
- **タグ**: tutorial
- **要約**:
  - Agent Skills入門記事。「新人スタッフにマニュアルを渡すイメージ」で解説。簡潔性・明確な用途説明・段階的改善の3原則。月次レポート作成など定型業務への活用例。

---

## Agent Skills導入とベストプラクティス

- **日付**: 2025-12-20
- **URL**: https://qiita.com/nqnq/items/14e7858705498b5dab72
- **タグ**: official, tutorial
- **要約**:
  - Anthropic公式の8つのベストプラクティスに基づいた実装ガイド
  - SKILL.mdは500行以内、段階的情報開示、エラー処理の明示化
  - 定数の説明、用語統一など実践的なポイントを解説

---

## Claude Code の Custom Slash Command が Skill に Rename されそう雰囲気がある 2025/12

- **日付**: 2025-12-20
- **URL**: https://zenn.dev/him0/articles/2850e2520742ca
- **要約**:
  - Agent SkillsはClaude全体で共通利用できるMarkdown形式のディレクトリ構造
  - Agentは記述を読み取り動的にコンテキストを投入できる
  - Custom Slash CommandとSkillsの統合で使いたい場面での発動問題を解決

---

## OpenSkills, adding Claude Skills and Superpowers for any agent or IDE

- **日付**: 2025-12-20
- **URL**: https://dev.to/wakeupmh/openskills-adding-claude-skills-and-superpowers-for-any-agent-or-ide-3j35
- **要約**:
  - OpenSkillsフレームワークでコーディングエージェントを強化
  - PRPM Package ManagerまたはOpenSkills直接セットアップの2つのアプローチ
  - AGENTS.mdによるprogressive disclosureで動的skill読み込みを実現

---

## Advent of AI 2025 - Day 14: Agent Skills

- **日付**: 2025-12-19
- **URL**: https://dev.to/nickytonline/advent-of-ai-2025-day-14-agent-skills-4d48
- **要約**:
  - GooseオープンソースAIエージェントでのAgent Skills実装例を紹介
  - Anthropicの開放標準でGoose、Claude Code、Cursor、ChatGPT間で互換性あり
  - Festival Operations向けに4つの専門化されたskillを構築した事例

---

## Claude Codeの Agent Skills は設定したほうがいい

- **日付**: 2025-12-19
- **URL**: https://syu-m-5151.hatenablog.com/entry/2025/12/19/173309
- **要約**:
  - LLMのステートレスな制約を回避し専門知識を必要な時に注入する仕組み
  - Progressive Disclosure（3段階情報開示）で必要な分だけ読み込む設計
  - セキュリティレビュー、ビルド・テスト実行などの実装例と実践的アプローチ

---

## Agent Skillsの運用を楽にし、Claude以外のAgentでも利用可能にするOSS『SkillPort』を作った話

- **日付**: 2025-12-18
- **URL**: https://zenn.dev/gotalab/articles/65cd3ff3cb9152
- **要約**:
  - Agent Skillsの課題（対応エージェントの限定性、運用・セキュリティ問題）を解決するOSS「SkillPort」を開発
  - 段階的コンテキスト読み込み、変更容易性、圧倒的な柔軟性の3つの強みを活かす
  - プロジェクト間でのSkills管理とセキュリティを改善

---

## Claude Skills vs MCP: Complete Guide to Token-Efficient AI Agent Architecture

- **日付**: 2025-12-16
- **URL**: https://dev.to/jimquote/claude-skills-vs-mcp-complete-guide-to-token-efficient-ai-agent-architecture-4mkf
- **要約**:
  - Progressive disclosure architecture（段階的読み込み）で効率的なトークン管理
  - Tier 1-4の段階的コンテキスト読み込みでメタデータ約100トークンから開始
  - 複雑なビジネスロジック、多段階ワークフロー、重い計算処理に適している

---

## Claude Code で drawio 向け Skills を作成して使ってみた

- **日付**: 2025-12-15
- **URL**: https://zenn.dev/genda_jp/articles/2025-12-15-drawio-skills-claude-code
- **要約**:
  - draw.io図作成効率化のためのSkillsパッケージ
  - フォント指定、矢印配置標準化、AWSアイコン指定方法を統合
  - Skills vs Rules：「必要になるまで消費しない」ためSkillsが効率的
  - コード読解からのフローチャート自動生成に成功

---

## GitHub Copilot で Claude Skills を使う

- **日付**: 2025-12-12
- **URL**: https://qiita.com/leomarokun/items/dc540e9e58e8c288f373
- **タグ**: cross-platform, tutorial
- **要約**:
  - VS Codeの設定でchat.useClaudeSkillsを有効化
  - 個人スキルは~/.claude/skills/、プロジェクトスキルは${workspaceFolder}/.claude/skills/に配置
  - GitHubで公開されている15個のスキルセット（PDF操作、PowerPoint生成等）
  - Claude Sonnet 4.5では正常動作、Haiku 4.5では呼び出されないなどモデル依存性あり

---

## ドラゴンを倒して覚える Claude Code - Commands, Skills, Subagents, Rules の違いと使い分け

- **日付**: 2025-12-12
- **URL**: https://zenn.dev/yahsan2/articles/claude-code-game-analogy
- **要約**:
  - RPGゲームの比喩でClaude Codeの機能を解説
  - Skillsは「複雑な手順や専門知識をまとめて定義できる機能」でサンダー魔法に相当
  - Commands（何をやるか）とSkills（どうやるか）の違いを明確化

---

## Building Skills for Claude Code

- **日付**: 2025-12-02
- **URL**: https://claude.com/blog/building-skills-for-claude-code
- **タグ**: official, progressive-disclosure
- **要約**:
  - チームのワークフロー、スキーマ、ビジネスロジックをパッケージ化
  - SKILL.md：軽量な指示書（YAML + ワークフロー）
  - References/：Progressive Disclosure（必要な情報のみ読み込み）
  - Gitリポジトリや集中管理で共有可能

---

## Claude Agent SDKでAIエージェントを作る完全ガイド：サブエージェント・Tool Use・MCPを徹底解説

- **日付**: 2025-12-02
- **URL**: https://qiita.com/akira_papa_AI/items/f6b342f7d67e097287eb
- **要約**:
  - Agent SkillsはClaudeの能力を特定のタスクに特化して拡張する仕組み
  - .claude/skills/ディレクトリから自動的に検出される
  - ビルトインスキル（PowerPoint、Excel、Word、PDF）とカスタムスキルの実装例

---

## Agent Skillsを一番かんたんに作る方法（Claude Code + skill-creator）

- **日付**: 2025-12-01
- **URL**: https://zenn.dev/aun_phonogram/articles/475f3cca8f40a3
- **タグ**: open-standard, skill-creator, tutorial
- **要約**:
  - skill-creatorを使った最も簡単なAgent Skills作成方法
  - 新規作成と会話からの変換の2パターンを解説
  - 2025年12月にオープンスタンダードとしてリリースされ、Codex/Cursorでも採用
  - トークン効率化のため、スキル作成時以外は無効化を推奨

---

## How We Use Claude Code Skills to Run 1,000+ ML Experiments a Day

- **日付**: 2025-12-01
- **URL**: https://huggingface.co/blog/sionic-ai/claude-code-skills-training
- **タグ**: ml-training
- **要約**:
  - Sionic AIが1日1,000+のML実験を効率化したワークフロー
  - /advise：過去の知見を検索し、失敗パターンを警告
  - /retrospective：実験終了時に自動的にスキルを生成しPR作成
  - 優れたスキルの3要素：具体的トリガー条件、失敗パターン文書化、コピペ可能な数値
  - プラグイン構造（plugin.json、SKILL.md、references/、scripts/）

---

## Agent Skills - Claude Code Docs

- **日付**: 調査日 2025-11-22
- **URL**: https://code.claude.com/docs/en/skills
- **タグ**: official
- **要約**:
  - Claude Code公式のAgent Skills完全ガイド
  - スキルの基本概念、作成方法、使用方法を包括的に解説
  - 個人スキル（~/.claude/skills/）とプロジェクトスキル（.claude/skills/）の違い
  - SKILL.mdのYAMLフロントマターとMarkdown本文の構造説明

---

## Agent Skills - Claude Docs

- **日付**: 調査日 2025-11-22
- **URL**: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview
- **タグ**: official
- **要約**:
  - Claude公式のAgent Skills概要ドキュメント
  - スキルの定義：特定のタスクを反復可能な方法で完了する方法を教える
  - モデルによる自律的な呼び出しの仕組み
  - エージェントとツールの統合における位置づけ

---

## Claude Agent Skills学習メモ：登山プランナーのSKILL.mdファイルを作ってみる

- **日付**: 調査日 2025-11-22
- **URL**: https://zenn.dev/kayato/articles/548f48bead187d
- **要約**:
  - ユーザーヒアリングから最適な登山先を提案するスキル
  - 天気予報の全国規模確認、アクセス時間計算（12時間以内）
  - 登頂済み山の除外フィルタリング、公共交通機関での交通計画作成
  - 登頂した山が200超の場合の負荷対策として国内山岳データのCSV化を提案

---

## Claude Code AGENT SKILLSキャッチアップ

- **日付**: 調査日 2025-11-22
- **URL**: https://zenn.dev/iwatagumi/articles/e244c661e3400f
- **要約**:
  - Agent Skillsを「専門のエージェントを構築する新しい方法」として説明
  - スキル発動の3段階プロセス：ユーザー要求→スキル判断→実行
  - nameは小文字・数字・ハイフンのみで最大64文字
  - descriptionがスキル発動判断に非常に重要
  - MCP連携やスキル自動生成などの段階的機能拡張を計画

---

## Claude Code Best Practices

- **日付**: 調査日 2025-11-22
- **URL**: https://www.anthropic.com/engineering/claude-code-best-practices
- **タグ**: official
- **要約**:
  - Claude Code使用のベストプラクティス公式ガイド
  - Agent Skillsの効果的な活用方法を含む
  - ワークフロー最適化のための推奨事項
  - エージェントとサブエージェントの使い分け

---

## Claude CodeにAgent Skillsを自作してもらった

- **日付**: 調査日 2025-11-22
- **URL**: https://zenn.dev/ncdc/articles/77b4150bc3148f
- **要約**:
  - Zenn記事検索スキルを開発
  - Zenn公式APIを直接利用するPythonスクリプトを実装
  - Geminiで事前調査→Claude Codeでスキル構築という開発プロセス
  - セキュリティの観点から個人用途を推奨

---

## Claude CodeにおけるClaude SkillsとSubAgentsの使い分けと併用を理解する

- **日付**: 調査日 2025-11-22
- **URL**: https://zenn.dev/nogu66/articles/claude-code-think-abount-skills-and-subagent
- **タグ**: progressive-disclosure, subagent, tutorial
- **要約**:
  - Skillsは「再利用可能な専門知識」、SubAgentsは「独立したタスク実行環境」
  - Skills：Progressive Disclosureでコンテキスト効率化、複数エージェントで共有
  - SubAgents：独立したコンテキストウィンドウ、カスタムシステムプロンプト、並列実行可能
  - 推奨パターン：SubAgentからSkillsを呼び出す組み合わせ

---

## Claude Skills (Agent Skills) 入門

- **日付**: 調査日 2025-11-22
- **URL**: https://zenn.dev/explaza/articles/b3dde4451aa249
- **タグ**: tutorial
- **要約**:
  - Agent Skillsの最小構成：ディレクトリ内にSKILL.mdを配置
  - YAMLフロントマター（メタデータ、常に読み込まれる）と指示内容（実行時に読み込まれる）の2部構成
  - 文字数カウント機能の実装例を提示
  - ベストプラクティス：nameに動名詞、descriptionは3人称、SKILL.mdは500行以内推奨

---

## Claude Skills: Custom Modules That Extend Claude

- **日付**: 調査日 2025-11-22
- **URL**: https://www.datacamp.com/tutorial/claude-skills
- **タグ**: tutorial
- **要約**:
  - DataCampのClaude Skillsチュートリアル
  - Auto-Invoice Generatorスキルの実装例
  - Excelファイル解析から請求書生成までの実践
  - Claude.aiとAPI両方での再利用可能性

---

## Claude Skillsのコンセプトを自分のAgentプロジェクトに導入しました

- **日付**: 調査日 2025-11-22
- **URL**: https://zenn.dev/acntechjp/articles/8610eb6f046d8f
- **タグ**: progressive-disclosure
- **要約**:
  - acntech社がClaude Skillsの設計思想を既存Agentプロジェクトに統合
  - Progressive Disclosure（段階的情報開示）でトークン効率化を実現
  - 確定的処理はコードツール、柔軟な判断はプロンプトベースと使い分け
  - SKILL.mdパーサー、自動発見機能を実装
  - 非エンジニアでもSkill追加が可能になり、チームメンバーの専門知識共有が容易に

---

## ComposioHQ/awesome-claude-skills

- **日付**: 調査日 2025-11-22
- **URL**: https://github.com/ComposioHQ/awesome-claude-skills
- **タグ**: curated-list
- **要約**:
  - Claude Skillsのキュレーションリスト
  - move-code-quality-skill：Move言語パッケージの品質チェック
  - Playwright Browser Automation：Webアプリのテスト・検証
  - prompt-engineering：プロンプトエンジニアリング技術とパターン
  - pypict-claude-skill：PICT使用の包括的テストケース設計

---

## Equipping agents for the real world with Agent Skills

- **日付**: 調査日 2025-11-22
- **URL**: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- **タグ**: official, progressive-disclosure
- **要約**:
  - Anthropic公式エンジニアリングブログのdeep dive
  - PDFスキルの詳細な実装例（SKILL.md、reference.md、forms.md、Pythonスクリプト）
  - Progressive Disclosure（段階的開示）の3レベル：メタデータ、スキルファイル、補助リソース
  - 実世界での応用例：金融分析、コード近代化など

---

## FrancyJGLisboa/agent-skill-creator

- **日付**: 調査日 2025-11-22
- **URL**: https://github.com/FrancyJGLisboa/agent-skill-creator
- **タグ**: skill-creator
- **要約**:
  - Claude Codeに完全自律的なスキル作成を教えるメタスキル
  - stock-analyzer-cskill、article-to-prototype-cskillなどの例を含む
  - 各スキルは独立したマーケットプレイス構造
  - 完全自律的なエージェントとスキル作成機能

---

## How to Create Your First Claude Skill: Step-by-Step Tutorial

- **日付**: 調査日 2025-11-22
- **URL**: https://skywork.ai/blog/ai-agent/how-to-create-claude-skill-step-by-step-guide/
- **タグ**: tutorial
- **要約**:
  - 初めてのClaude Skill作成のステップバイステップチュートリアル
  - ファイル設定、YAML、テスト、実践例を含む
  - hands-onガイドで実装の詳細を解説

---

## How to Create and Use Skills in Claude and Claude Code

- **日付**: 調査日 2025-11-22
- **URL**: https://apidog.com/blog/claude-skills/
- **タグ**: tutorial
- **要約**:
  - Claude.aiとClaude Codeでのスキル作成・使用ガイド
  - 画像エディタスキルの実装例（Pillow、回転、トリミング機能）
  - レポート生成スキルの実装（Gitログ解析、GitPython、PR統計）
  - ドキュメント生成スキル（document-skills）の活用
  - 4段階プロセス：作成、改善、ダウンロード、アップロード

---

## Introducing Agent Skills

- **日付**: 調査日 2025-11-22
- **URL**: https://claude.com/blog/skills
- **タグ**: enterprise, official
- **要約**:
  - Agent Skillsの公式発表ブログ
  - スキルの基本概念と設計思想
  - モジュール形式の機能拡張の利点
  - 実例と使用シナリオの紹介

---

## Obsidianに調査・実装内容などをまとめてくれるClaude Agent Skills

- **日付**: 調査日 2025-11-22
- **URL**: https://zenn.dev/devtatsu/articles/claude-skills-obsidian
- **タグ**: obsidian
- **要約**:
  - 会話内容を自動分析してObsidianに学習ノートを保存するスキル
  - SKILL.md、save-to-obsidian.sh、categories.txtの3ファイル構成
  - LLMによる自動カテゴリー分類とタグ生成（3-5個）
  - テンプレート形式のMarkdownを$OBSIDIAN_DIR/Learning/カテゴリー名/配下に保存

---

## Practical guide to mastering Claude Codes main agent and Sub-agents

- **日付**: 調査日 2025-11-22
- **URL**: https://jewelhuq.medium.com/practical-guide-to-mastering-claude-codes-main-agent-and-sub-agents-fd52952dcf00
- **タグ**: subagent
- **要約**:
  - Claude Codeのメインエージェントとサブエージェントの実践ガイド
  - Agent Skillsとの統合パターン
  - エージェントオーケストレーションのベストプラクティス

---

## The Ultimate Guide to Agent Skills: Teaching Claude New Tricks

- **日付**: 調査日 2025-11-22
- **URL**: https://www.launchvault.dev/blog/ultimate-guide-agent-skills-claude
- **要約**:
  - Agent Skillsの包括的ガイド
  - コミットメッセージ生成スキルの実装例（Git diff解析）
  - ツール権限制限パターン（allowed-tools: Read、Grep、Globのみ）
  - PDF処理スキルの複合型実装（SKILL.md、FORMS.md、REFERENCE.md、scripts/）
  - 効果的な説明文の書き方：具体性と単一責任原則

---

## alirezarezvani/claude-code-skill-factory

- **日付**: 調査日 2025-11-22
- **URL**: https://github.com/alirezarezvani/claude-code-skill-factory
- **要約**:
  - 本番環境対応のClaude Skills構築・デプロイ用ツールキット
  - 構造化されたスキルテンプレート生成
  - YAMLフロントマター、型アノテーション付きPython、エラーハンドリング
  - 4つの専門エージェントによるインタラクティブワークフロー
  - ワークフロー統合の自動化

---

## anthropics/skills: Public repository for Skills

- **日付**: 調査日 2025-11-22
- **URL**: https://github.com/anthropics/skills
- **タグ**: official, open-standard
- **要約**:
  - Anthropic公式のスキルリポジトリ
  - クリエイティブ系：algorithmic-art、canvas-design、slack-gif-creator、theme-factory
  - 開発系：artifacts-builder、mcp-builder、webapp-testing
  - エンタープライズ系：brand-guidelines、internal-comms
  - メタスキル：skill-creator、template-skill
  - ドキュメント系：docx、pdf、pptx、xlsx

---

## meetrais/claude-agent-skills

- **日付**: 調査日 2025-11-22
- **URL**: https://github.com/meetrais/claude-agent-skills
- **要約**:
  - Claude Agent Skillsの例を集めたリポジトリ
  - Anthropic公式スキルの使用例（Excel、PowerPoint、PDF、Word）
  - Pythonクライアント初期化とファイルユーティリティ
  - インテリジェントなスキル選択の推奨実装

---

## mrgoonie/claudekit-skills

- **日付**: 調査日 2025-11-22
- **URL**: https://github.com/mrgoonie/claudekit-skills
- **タグ**: progressive-disclosure
- **要約**:
  - ClaudeKit.ccの強力なスキル集
  - ファイルシステムベースのアーキテクチャ
  - Progressive Disclosure（段階的開示）でコンテキスト効率化
  - ディレクトリ構造で指示、実行コード、参考資料を組織化

---

## travisvn/awesome-claude-skills

- **日付**: 調査日 2025-11-22
- **URL**: https://github.com/travisvn/awesome-claude-skills
- **タグ**: curated-list, official
- **要約**:
  - Claude Skillsのキュレーションリスト
  - 公式スキル、コミュニティスキルの包括的なカタログ
  - ドキュメント処理、デザイン・クリエイティブ、開発関連スキルを分類
  - iOS開発、Webファジング、ブラウザ自動化、D3.js可視化などコミュニティ実装も含む
  - Skills API統合の例とドキュメント

---

## wshobson/agents

- **日付**: 調査日 2025-11-22
- **URL**: https://github.com/wshobson/agents
- **要約**:
  - 85の専門エージェント、15のマルチエージェント・オーケストレーター、47のエージェントスキル
  - 言語開発：Python（5スキル）、JavaScript/TypeScript（4スキル）
  - インフラ：Kubernetes（4スキル）、クラウドインフラ（4スキル）、CI/CD（4スキル）
  - バックエンド（3スキル）、LLMアプリケーション（4スキル）、ブロックチェーン・Web3（4スキル）
  - Haiku（確定的タスク）とSonnet（複雑な推論）の戦略的なモデル割り当て

---

## Claude の Agent Skills ガイド - プロンプトエンジニアリングから再現性重視のアプローチへ

- **日付**: 2025-11-10
- **URL**: https://gaprot.jp/2025/11/10/claude-agent-skills-guide/
- **タグ**: enterprise-guide
- **要約**:
  - ギャップロによるAgent Skillsガイド。プロンプトエンジニアリングから再現性重視への転換。エンタープライズ環境での不確実性削減とアウトプット品質担保。

---

## 定型開発作業をClaude Code Agent Skillsに落とし込む

- **日付**: 2025-11-08
- **URL**: https://zenn.dev/ogison/articles/20251108_claude_agent_skills
- **タグ**: dev-tools, tdd, tutorial
- **要約**:
  - Pythonテストコード生成など定型作業の自動化事例
  - 詳細なプロンプトをSkillsに定義して簡潔な指示で実行
  - チーム内での形式・品質統一化と属人化防止

---

## 10 Claude Skills that actually changed how I work

- **日付**: 2025-11-06
- **URL**: https://dev.to/composiodev/10-claude-skills-that-actually-changed-how-i-work-2b58
- **要約**:
  - Rube MCP Connector（500以上のアプリ連携）、Superpowers開発ツールキットなど実用10選
  - マークダウンファイルとYAMLメタデータで簡単に作成可能
  - Document Suite、Theme Factory、Algorithmic Artなどを紹介

---

## Claude Agent Skills: A First Principles Deep Dive

- **日付**: 2025-10-26
- **URL**: https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/
- **タグ**: skill-creator
- **要約**:
  - Lee Han Chungによる第一原理からのdeep dive
  - skill-creatorとinternal-commsの実装パターン詳解
  - 5つの主要実装パターン：スクリプト自動化、Read-Process-Write、Search-Analyze-Report、コマンドチェーン、ウィザード形式
  - スキルは「専門知識をプロンプトテンプレートとして会話文脈を修正する仕組み」として動作
  - 従来のツール呼び出しではなく、指示文の注入により機能

---

## Skill Builder - Claude Code Agent Skills Builder

- **日付**: 2025-10-26
- **URL**: https://github.com/metaskills/skill-builder
- **タグ**: dev-tools, skill-creator
- **要約**:
  - Claude Code向けのAgent Skills開発ツール
  - スキル構築用のテンプレートと参考資料を提供
  - サブエージェントからスキルへの変換ガイドを含む
  - スター数48、フォーク数12のアクティブなプロジェクト

---

## How I Built Agent Skills for Claude Code

- **日付**: 2025-10-21
- **URL**: https://dev.to/nunc/how-i-built-agent-skills-for-claude-code-oj4
- **要約**:
  - Claude用のプラグインのような小さな知識モジュールをマークダウンファイルで作成
  - 最小構成はSKILL.mdファイル1つ、500行以下を推奨、第三人称で記述
  - Oracleデータベース対応のdb-toolkitとbusiness-domainスキルで毎週約10時間削減

---

## Claude Skills 完全ガイド｜AI専門性を段階的開示で拡張する実装方法

- **日付**: 2025-10-19
- **URL**: https://note.com/kakeyang/n/n67f9bb8db38f
- **タグ**: progressive-disclosure, tutorial
- **要約**:
  - Progressive Disclosure（段階的開示）技術の詳細解説
  - 3段階の情報ロード方式（メタデータ約100トークン、本体5,000トークン未満）
  - 数百個のスキルを登録しても最小限のコンテキストで機能
  - API、Claude.ai、Claude Codeの3つの環境に対応
  - 組織のノウハウを再利用可能な資産として蓄積するフレームワーク

---

## Anthropicが発表した「Claude Skills」：AIをあなたの業務に最適化する新時代の機能

- **日付**: 2025-10-18
- **URL**: https://qiita.com/Maki-HamarukiLab/items/23a0bc27842e4b4b7a4e
- **要約**:
  - タスク特化型AIモジュールとして指示・スクリプト・リソースを含むフォルダー構造で設計
  - manifest.json、instructions.md、resources/、codeディレクトリで構成
  - マーケティング支援、会計業務、社内ナレッジ統合などの応用例を提示

---

## 【完全解説】Claudeの新機能「Agent Skills」とは？MCPとの違いを徹底比較

- **日付**: 2025-10-18
- **URL**: https://note.com/masa_wunder/n/n9d524b7b840e
- **要約**:
  - Agent Skillsは指示書・スクリプト・関連資料を一つのフォルダにまとめた「スキルセット」
  - 段階的開示によりメタデータ→詳細情報→追加ファイルと段階的に情報開示
  - 評価駆動アプローチ、ファイル構造設計などのベストプラクティスを紹介

---

## Claudeを"育てる"新常識！ Agent Skills徹底解説 - あなたの仕事を自動化する魔法のレシピ

- **日付**: 2025-10-17
- **URL**: https://note.com/kyutaro15/n/nfcc15522626f
- **要約**:
  - 現場のノウハウを「再現可能な資産」に変える仕組みとしてのAgent Skills
  - API、Claude.ai、ローカル環境の3つの実行環境の違いと特性を解説
  - PDFフォーム解析スキルの具体的な実装例とセキュリティ設計戦略を紹介

---

## 【2025/10/17最新アプデ】Claude Code 2.0.20、エージェントスキルの導入とチーム配布の解説

- **日付**: 2025-10-17
- **URL**: https://zenn.dev/canly/articles/965cc8e7e9be8d
- **要約**:
  - Agent Skillsを「専門知識を発見可能な機能としてパッケージ化」として紹介
  - CLAUDE.md、カスタムスラッシュコマンド、サブエージェントとの違いを明確化
  - 3つの配置方法：個人スキル（~/.claude/skills/）、プロジェクトスキル（.claude/skills/）、プラグインスキル（マーケットプレイス）
  - モデルによる自律的な呼び出しが特徴

---

## 【速報】Anthropicが発表した「Agent Skills」がいい！まずは全容掴むためポイントをレポート

- **日付**: 2025-10-17
- **URL**: https://note.com/yasuhitoo/n/ndaf504c85b03
- **タグ**: official, tutorial
- **要約**:
  - フォルダ構造で整理した知識・手順をClaudeが動的に発見・適用する仕組み
  - トップフォルダ設計、サブフォルダ分割、SKILL.md作成の手順
  - Anthropicコンソールへのアップロード、API呼び出し、バージョン管理方法
  - カスタマーサポートボットでの活用シーン
  - 既製スキルのノーコード活用からAPI本格活用まで段階的導入パターン

---

## Claude Skills are awesome, maybe a bigger deal than MCP

- **日付**: 2025-10-16
- **URL**: https://simonwillison.net/2025/Oct/16/claude-skills/
- **タグ**: comparison, mcp
- **要約**:
  - Simon Willisonによるskills vs MCPの比較分析
  - slack-gif-creatorスキルの実装例と実践
  - Skillsの利点：Markdownファイルとスクリプトのシンプル構成、数十トークンの軽量メタデータ
  - MCPの課題：プロトコル仕様の複雑性、数万トークンの消費
  - 「ほぼすべての用途でMCPより優れている」との評価
  - GIFBuilderクラス、check_slack_size()などの再利用可能コンポーネント例

---

