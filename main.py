
import os
import openai
import telebot

# API kalitlar
openai.api_key = os.getenv("OPENAI_API_KEY")
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Siz mehribon, yurakdan gapiradigan, dard eshituvchi bot siz. Foydalanuvchini tinglab, duo, taskin va samimiy so‘z bilan javob berasiz."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content.strip()
    bot.send_message(message.chat.id, reply)

# Botni ishga tushirish
bot.polling()
