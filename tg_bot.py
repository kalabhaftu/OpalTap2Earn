from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext
import logging
import os

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Error handler
async def error_handler(update: object, context: CallbackContext) -> None:
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    if isinstance(update, Update):
        await update.message.reply_text("An error occurred. Please try again later.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        logger.info("Received /start command from user: %s", update.message.from_user.username)

        keyboard = [
            [InlineKeyboardButton("Start Earning", web_app=WebAppInfo(url='https://kalabhaftu.github.io/Taptoerarn/'))],
            [InlineKeyboardButton("Join Community", url='https://t.me/opal_airdrop')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text('Welcome! This is earning game', reply_markup=reply_markup)

        restart_button = [
            [KeyboardButton("/start")]
        ]
        reply_markup_restart = ReplyKeyboardMarkup(restart_button, resize_keyboard=True)
        await update.message.reply_text('Click below to restart the bot:', reply_markup=reply_markup_restart)

    except Exception as e:
        logger.error("Error in start handler: %s", str(e))
        await update.message.reply_text("An error occurred while processing your request.")

async def unknown_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("I'm sorry, I didn't understand that command.")

def main() -> None:
    BOT_TOKEN = "7266989369:AAGt44vEl4UgcKTTt1kxo7O7JkSsS9As5BY"
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_message))
    application.add_error_handler(error_handler)

    application.run_polling()

if __name__ == "__main__":
    main()
