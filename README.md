# Discord Bot - ゆーまおだよ‼️

「ゆーまおさん」って送ると「ゆーまおだよ」って返すDiscord Botです。

## 必要なもの

- Python 3.12以上
- uv (Pythonパッケージマネージャー)
- Discord Bot Token

## セットアップ

### 1. uvのインストール

```bash
pip install uv
```

### 2. 依存関係のインストール

```bash
uv sync
```

### 3. Discord Bot Tokenの設定

1. [Discord Developer Portal](https://discord.com/developers/applications)でBotを作成
2. Bot Tokenを取得
3. `.env.example`を`.env`にコピー
4. `.env`ファイルにTokenを設定

```bash
cp .env.example .env
# .envファイルを編集してDISCORD_BOT_TOKENを設定
```

または、環境変数として設定：

```bash
export DISCORD_BOT_TOKEN=your_token_here
```

### 4. Botの実行

```bash
uv run python main.py
```

または：

```bash
python main.py
```

## 使い方

1. BotをDiscordサーバーに招待
2. 任意のチャンネルで「ゆーまおさん」と送信
3. Botが「ゆーまおだよ」と返信します

## Bot Permissions

Bot招待時に以下の権限が必要です：
- Read Messages/View Channels
- Send Messages
- Read Message History

## 注意事項

- `.env`ファイルはGitにコミットしないでください（.gitignoreに含まれています）
- Bot TokenはDiscord Developer Portalで再生成できます

