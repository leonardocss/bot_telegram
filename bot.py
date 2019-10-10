import telebot
import random
from telebot.types import Message

TOKEN = '945149843:AAFRj55o7Es1YlgKDGEN9zldBj0My2zyNvs'
STICKER_ID = ''
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def command_handler(message: Message):
  bot.reply_to(message, 'There is no answer')

@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
  if 'Alex good kid' in message.text:
    bot.reply_to(message, str('Alex if good KID'))
    return
  bot.reply_to(message, str(random.random()))

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
  print(message)
  print(message.sticker)



bot.polling(timeout=60)