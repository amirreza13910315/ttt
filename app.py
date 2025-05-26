from flask import Flask, request
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters
import os
from dotenv import load_dotenv
import random
from database.db import Database
from data.foods import IRANIAN_FOODS
from utils.keyboards import get_main_keyboard, get_admin_keyboard
from handlers.command_handlers import start, help_command
from handlers.callback_handlers import handle_callback
from handlers.message_handlers import handle_message
from handlers.admin_handlers import handle_admin_message

load_dotenv()

app = Flask(__name__)
db = Database()

# Initialize bot
bot = Application.builder().token(os.getenv('BOT_TOKEN')).build()

# Add handlers
bot.add_handler(CommandHandler('start', start))
bot.add_handler(CommandHandler('help', help_command))
bot.add_handler(CallbackQueryHandler(handle_callback))
bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

@app.route('/' + os.getenv('BOT_TOKEN'), methods=['POST'])
async def webhook():
    update = Update.de_json(request.get_json(), bot)
    await bot.process_update(update)
    return 'OK'

@app.route('/')
def index():
    return 'Bot is running!'

if __name__ == '__main__':
    # Set webhook
    bot.set_webhook(os.getenv('WEBHOOK_URL') + os.getenv('BOT_TOKEN'))
    # Start Flask server
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))