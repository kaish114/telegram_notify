# Telegram Notify

A simple Python package for sending notifications via Telegram.

## Installation

```bash
pip install git+https://github.com/kaish114/telegram_notify.git
```

Or install from source:

```bash
git clone https://github.com/kaish114/telegram_notify.git
cd telegram-notify
pip install -e .
```

## Configuration

You need to set the following environment variables:

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
- `TELEGRAM_CHANNEL_ID`: The chat or channel ID where notifications will be sent

You can set these in a `.env` file in your project root:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHANNEL_ID=your_chat_id_here
```

## Usage

```python
from telegram_notify import send_notification

# Basic usage with environment variables
send_notification("Hello from Telegram Notify!")

# Or provide credentials directly
send_notification(
    message="Hello from Telegram Notify!",
    bot_token="your_bot_token_here",
    chat_id="your_chat_id_here"
)
```

## Requirements

- Python 3.6+
- python-telegram-bot
- python-dotenv