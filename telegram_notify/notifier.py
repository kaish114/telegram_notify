import os
import logging
from telegram import Bot
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def send_notification(message: str, bot_token: str = None, chat_id: str = None) -> None:
    """
    Sends a notification to the configured Telegram chat or channel.
    
    Args:
        message: The message to send.
        bot_token: Optional Telegram bot token. If not provided, will be read from TELEGRAM_BOT_TOKEN env var.
        chat_id: Optional chat or channel ID. If not provided, will be read from TELEGRAM_CHANNEL_ID env var.
        
    Raises:
        ValueError: If bot_token or chat_id is not provided and not found in environment variables.
        Exception: If sending the notification fails.
    """
    # Get credentials from parameters or environment variables
    telegram_bot_token = bot_token or os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = chat_id or os.getenv('TELEGRAM_CHANNEL_ID')
    
    # Validate credentials
    if not telegram_bot_token or not telegram_chat_id:
        raise ValueError("Telegram bot token or chat ID is not provided and not set in environment variables.")
    
    try:
        bot = Bot(token=telegram_bot_token)
        bot.send_message(chat_id=telegram_chat_id, text=message)
        logger.info(f"Notification sent: {message}")
    except Exception as e:
        logger.error(f"Failed to send notification: {e}")
        raise