
import os
import telebot
import openai

# OpenAI va Telegram kalitlarini olish
openai.api_key = os.getenv("OPENAI_API_KEY")
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

# Har bir foydalanuvchi xabariga javob
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Siz dard eshitadigan, taskin beradigan yurakli bot siz. Foydalanuvchini samimiy tinglab, yurakdan javob bering."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content.strip()
    bot.send_message(message.chat.id, reply)

# Botni ishga tushirish
bot.polling()
