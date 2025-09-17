import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Get the token from Render environment variables
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! I am your Telegram meme detection bot.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

def main():
    if not TOKEN:
        raise ValueError("❌ TELEGRAM_TOKEN not found in environment variables!")

    # Create the application with the correct builder
    app = Application.builder().token(TOKEN).build()

    # /start command
    app.add_handler(CommandHandler("start", start))

    # Reply to any text message
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot started! Waiting for Telegram messages...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
