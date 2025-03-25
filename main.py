
import os
import openai
import telebot

# Kalitlar
openai.api_key = os.getenv("OPENAI_API_KEY")
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

# Har bir foydalanuvchi xabari uchun javob
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    # OpenAI modelga murojaat
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Siz mehribon, muloyim, yurakdan so'zlaydigan dard eshituvchi bot siz. Foydalanuvchini hech qachon hukm qilmaymiz, faqat taskin, duo, tushunish bilan javob beramiz."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content.strip()
    bot.send_message(message.chat.id, reply)

# Botni ishga tushirish
bot.polling()
