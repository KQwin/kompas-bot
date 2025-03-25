
import os
import telebot
from openai import OpenAI

# API kalitlar
openai_api_key = os.getenv("OPENAI_API_KEY")
telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(telegram_token)
client = OpenAI(api_key=openai_api_key)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Siz yurakni eshitadigan, samimiy, mehribon bot siz. Foydalanuvchining dardini tinglab, taskinli so'zlar bilan javob bering."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content.strip()
    bot.send_message(message.chat.id, reply)

bot.polling()
