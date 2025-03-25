import os
import telebot
import openai

# Kalitlar
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))
openai.api_key = os.getenv("OPENROUTER_API_KEY")

# Har bir xabar uchun javob
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    "Sen Mehribonim deb murojaat qiladigan, mehrli, yurakdan so‘zlaydigan, yupatadigan va halol botisan. "
                    "Hech qachon hukm qilma. Faqat taskin, duo va hayotiy donolik bilan javob qaytar. "
                    "Foydalanuvchini Mehribonim deb atagin, va har bir javob boshida shu so‘zni ishlat."
                )
            },
            {"role": "user", "content": user_input}
        ]
    )

    bot.reply_to(message, response.choices[0].message.content.strip())

# Ishga tushirish
bot.polling()
