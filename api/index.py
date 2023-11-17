import os
from typing import Optional
from fastapi import FastAPI,Request
from pydantic import BaseModel

# TELEGRAM
from telegram import Update,Bot
from telegram.ext import Dispatcher,MessageHandler ,Filters,CommandHandler



TOKEN = os.environ.get("TOKEN")

TOKEN = "6121025171:AAEF2n8BfnmWsrp_vkajprGrffwBFYAtpFg"
app =FastAPI()

class TelegramWebHook(BaseModel):
    updated_at:int
    message: Optional[dict]
    edited_message:Optional[dict]
    channel_post:Optional[dict]
    edited_channel_post: Optional[dict]

    inline_query: Optional[dict]
    chosen_inline_result: Optional[dict]
    callback_query: Optional[dict]
    shipping_query: Optional[dict]
    pre_checkout_query: Optional[dict]
    #poll request infos
    poll: Optional[dict]
    poll_answer: Optional[dict]

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to my-horoscope bot!")

def register_handlers(dispatcher):
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

@app.post("/webhook")
def webhook(webhook_data:TelegramWebHook):
    bot =Bot(token=TOKEN)
    update = Update.de_json(webhook_data.__dict__,bot)
    dispatcher = Dispatcher(bot,None,workers=4)
    register_handlers(dispatcher=dispatcher)

    dispatcher.process_update(update)
    return {"message":"OK"}

@app.get("/")
def index():
    return {"message": "Hello World"}





