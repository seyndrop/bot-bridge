import asyncio
import subprocess
import tempfile
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

with open("config.json", "r") as f:
    config = json.load(f)
TELEGRAM_TOKEN = config["telegram_token"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь токен Discord-бота для запуска.")

async def handle_token(update: Update, context: ContextTypes.DEFAULT_TYPE):
    token = update.message.text.strip()
    await update.message.reply_text("Запускаю Discord-бота на 5 минут...")

    with open("dbot.py", "r") as template_file:
        bot_code = template_file.read().replace("DISCORD_TOKEN", token)
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
        tmp.write(bot_code)
        bot_path = tmp.name

    process = subprocess.Popen(["python", bot_path])
    await asyncio.sleep(300)  
    process.terminate()

    await update.message.reply_text("Discord-бот остановлен.")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_token))

if __name__ == "__main__":
    app.run_polling()