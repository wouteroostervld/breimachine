from flask import Flask, request
from config import TOKEN
import telegram

app = Flask(__name__)

bot = telegram.Bot(token=TOKEN)

@app.route('/', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text

    # repeat the same message back (echo)
    bot.sendMessage(chat_id=chat_id, text=text)
    return 'OK'

if __name__ == '__main__':
    app.run()
