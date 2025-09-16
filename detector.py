import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Récupère le token depuis les variables d'environnement Render
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salut ! Je suis ton bot Telegram de détection de mèmes.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Tu as dit : {update.message.text}")

def main():
    app = Application.builder().token(TOKEN).build()

    # Commande /start
    app.add_handler(CommandHandler("start", start))
    # Répète tout texte envoyé
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot lancé ! En attente de messages Telegram...")
    app.run_polling(close_loop=False)

if __name__ == "__main__":
    main()
