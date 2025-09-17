import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Récupère le token depuis Render
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Répond à la commande /start"""
    await update.message.reply_text("👋 Salut ! Je suis ton bot Telegram de détection de mèmes.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Répète les messages envoyés par l'utilisateur"""
    await update.message.reply_text(f"Tu as dit : {update.message.text}")

def main():
    if not TOKEN:
        raise ValueError("❌ TELEGRAM_TOKEN non trouvé dans les variables d'environnement !")

    # Crée l'application avec le builder moderne
    app = Application.builder().token(TOKEN).build()

    # Commande /start
    app.add_handler(CommandHandler("start", start))

    # Répond à tout message texte
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Bot lancé ! En attente de messages Telegram...")
    app.run_polling()

if __name__ == "__main__":
    main()
