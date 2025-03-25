
import os
import telebot
import httpx

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://yourdomain.com",
        "X-Title": "Ruhiy Kompas"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Sen mehribon, dono, yurakdan gapiradigan, yurakni yupatadigan bot bo‘lishing kerak. "
                    "Foydalanuvchining dardi bo‘lsa, unga tasalli ber, maslahat ber, ammo hech qachon hukm qilma. "
                    "Yaxshi ko‘r, eshit, tushun, va soxta emas — chin yurakdan gapir. "
                    "Yordam so‘raganlar qalbida umid uyg‘ot, duo ayt, yuragini yengillashtir."
                )
            },
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = httpx.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        completion = response.json()
        reply = completion["choices"][0]["message"]["content"]
        bot.send_message(message.chat.id, reply)
    except Exception as e:
        bot.send_message(message.chat.id, "Kechirasiz, yuragingizni eshita olmadim. Qayta urinib ko‘ring, men shu yerdaman.")

bot.polling()
