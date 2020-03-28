from flask import Flask, request
from config import TOKEN
import telegram
from telegram.ext import Dispatcher, CommandHandler
from requests import get

app = Flask(__name__)

bot = telegram.Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None)

def get_stats_for(country="Netherlands"):
    for stats in get("https://api.covid19api.com/summary").json()["Countries"]:
        if stats["Country"] == country:
            return stats
    return None 
        
def report_stats_for(country="Netherlands"):
    stats = get_stats_for(country)
    report = "Corona (COVID-19) stats for {}:\n\n".format(country)
    for k,v in stats.items():
        report += "    {}: {}\n".format(k, v)
    return report
    
def stats(bot, update):
    report = report_stats_for()
    update.message.reply_text(report)

@app.route('/', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'OK'

dispatcher.add_handler(CommandHandler("stats", stats))

if __name__ == '__main__':
    app.run()
