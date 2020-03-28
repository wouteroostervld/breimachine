#!/bin/env python
import telegram
from config import TOKEN
from sys import argv, exit

bot = telegram.Bot(token=TOKEN)
result = bot.setWebhook(argv[1])
if not result:
    exit(1)
