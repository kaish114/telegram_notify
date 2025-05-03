# telegram_notify

<div align="center">

![Telegram Notify Logo](https://via.placeholder.com/200x200.png?text=Telegram+Notify)

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-latest-blue.svg)](https://python-telegram-bot.org/)
[![PyPI](https://img.shields.io/badge/PyPI-Installation-green.svg)](https://pypi.org/project/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**A lightweight Python package for sending Telegram notifications**

[Installation](#installation) • 
[Usage](#usage) • 
[Configuration](#configuration) • 
[Examples](#examples) • 
[API Reference](#api-reference)

</div>

## 🌟 Overview

`telegram_notify` is a simple, elegant Python package for sending notifications via Telegram. Designed to be minimal yet powerful, it allows developers to easily integrate Telegram notifications into any Python application with just a few lines of code.

## 🚀 Installation

### From GitHub (Recommended)

```bash
pip install git+https://github.com/kaish114/telegram_notify.git
```

### From Source

```bash
git clone https://github.com/kaish114/telegram_notify.git
cd telegram-notify
pip install -e .
```

## ⚙️ Configuration

You can configure `telegram_notify` in two ways:

### 1. Environment Variables (Recommended)

Set the following environment variables:

```bash
# Add to your .env file or export directly
export TELEGRAM_BOT_TOKEN=your_bot_token_here
export TELEGRAM_CHANNEL_ID=your_chat_id_here
```

or create a `.env` file in your project root:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHANNEL_ID=your_chat_id_here
```

### 2. Direct Parameter Passing

Alternatively, provide credentials directly with each notification:

```python
send_notification(
    message="Your message here",
    bot_token="your_bot_token_here",
    chat_id="your_chat_id_here"
)
```

## 📋 Usage

### Basic Usage

```python
from telegram_notify import send_notification

# Using environment variables
send_notification("Hello from Telegram Notify!")

# With explicit credentials
send_notification(
    message="Hello from Telegram Notify!",
    bot_token="your_bot_token_here",
    chat_id="your_chat_id_here"
)
```

### Message Formatting

```python
# Plain text
send_notification("Simple text message")

# Markdown formatting
send_notification(
    "Message with *bold* and _italic_ text",
    parse_mode="Markdown"
)

# HTML formatting
send_notification(
    "Message with <b>bold</b> and <i>italic</i> text",
    parse_mode="HTML"
)
```

## 💡 Examples

<details>
<summary><b>System Monitoring Alerts</b></summary>

```python
import psutil
from telegram_notify import send_notification

def check_disk_space():
    disk = psutil.disk_usage('/')
    percent_free = disk.free / disk.total * 100
    
    if percent_free < 10:
        send_notification(
            f"🚨 WARNING: Low disk space!\n"
            f"Only {percent_free:.1f}% available on main disk.\n"
            f"Free: {disk.free / (1024**3):.1f} GB\n"
            f"Total: {disk.total / (1024**3):.1f} GB"
        )
```
</details>

<details>
<summary><b>Application Error Reporting</b></summary>

```python
import traceback
from telegram_notify import send_notification

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_message = f"❌ ERROR in {func.__name__}:\n"
            error_message += f"Type: {type(e).__name__}\n"
            error_message += f"Message: {str(e)}\n"
            error_message += f"Stack Trace:\n"
            error_message += f"```\n{traceback.format_exc()}```"
            
            send_notification(error_message, parse_mode="Markdown")
            raise  # Re-raise the exception after notification
    return wrapper

@error_handler
def process_data(data):
    # Process data here
    result = 10 / 0  # Will cause a ZeroDivisionError
    return result
```
</details>

<details>
<summary><b>Scheduled Reports</b></summary>

```python
import schedule
import time
from datetime import datetime
from telegram_notify import send_notification

def send_daily_report():
    today = datetime.now().strftime("%Y-%m-%d")
    report = f"📊 Daily Report ({today})\n\n"
    report += "✅ System Status: Operational\n"
    report += "📈 New Users: 25\n"
    report += "💰 Revenue: $1,245.67\n"
    report += "🔄 Processed Transactions: 152"
    
    send_notification(report)

# Schedule the report to run daily at 8:00 AM
schedule.every().day.at("08:00").do(send_daily_report)

while True:
    schedule.run_pending()
    time.sleep(60)
```
</details>

## 📚 API Reference

### `send_notification`

```python
def send_notification(
    message: str,
    bot_token: Optional[str] = None,
    chat_id: Optional[str] = None,
    parse_mode: Optional[str] = None,
    disable_notification: bool = False,
    disable_web_page_preview: bool = True
) -> bool:
    """
    Send a notification message to a Telegram chat.
    
    Args:
        message (str): The message text to send
        bot_token (str, optional): Telegram bot token. If None, uses TELEGRAM_BOT_TOKEN env var
        chat_id (str, optional): Chat ID to send the message to. If None, uses TELEGRAM_CHANNEL_ID env var
        parse_mode (str, optional): Parse mode for message formatting (Markdown, HTML)
        disable_notification (bool): Send message silently if True
        disable_web_page_preview (bool): Disable link previews if True
        
    Returns:
        bool: True if the message was sent successfully, False otherwise
    """
```

## 🧩 Integration with TensorQuark

`telegram_notify` is used across the TensorQuark platform components:

- **TQB (Backend)**: For order execution notifications and system alerts
- **TQTB (Telegram Bot)**: For responding to user commands via Telegram
- **Monitoring Services**: For alerting on system events and errors

## 🤝 Contributing

Contributions to `telegram_notify` are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to your branch: `git push origin feature/amazing-feature`
5. Open a pull request

## 📝 Requirements

- Python 3.6+
- python-telegram-bot
- python-dotenv

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For questions or feedback, please reach out:

- **Email**: iiitu17131@gmail.com
- **GitHub**: [kaish114](https://github.com/kaish114)

---

<div align="center">
  <p>Built with ❤️ by the TensorQuark Team</p>
</div>