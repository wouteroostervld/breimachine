from flask import Flask, request
from config import TOKEN
import telegram
from telegram.ext import Dispatcher, CommandHandler
from requests import get

app = Flask(__name__)

bot = telegram.Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None)

def get_stats_for(target_country="Netherlands"):
    countries=get("https://api.covid19api.com/summary").json()["Countries"]
    for country in countries:
        if country["Country"] == target_country:
            return country
    return "Not found"
        
        
    
def stats(bot, update):
    update.message.reply_text(str(get_stats_for()))

@app.route('/', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'OK'

dispatcher.add_handler(CommandHandler("stats", stats))

if __name__ == '__main__':
    app.run()
