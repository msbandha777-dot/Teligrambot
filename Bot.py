
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome!\n\n"
        "Bot is working successfully. ✅"
    )

def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        print("BOT_TOKEN is not set!")
        return

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
