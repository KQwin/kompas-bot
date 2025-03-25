import os
from openai import OpenAI
import telebot

# API kalitlari
openai_api_key = os.getenv("OPENAI_API_KEY")
telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")

client = OpenAI(api_key=openai_api_key)
bot = telebot.TeleBot(telegram_token)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Sen mehribon, tushunadigan, samimiy suhbatdosh botsan. Foydalanuvchiga 'Mehribonim' deb murojaat qil."},
            {"role": "user", "content": user_input}
        ]
    )
    bot.reply_to(message, response.choices[0].message.content)

bot.infinity_polling()
