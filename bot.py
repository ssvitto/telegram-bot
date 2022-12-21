import telebot
from telebot import types
import os

bot = telebot.TeleBot('5705294838:AAHgHNsKtjYnJ-jNw6YQeKv_v26PAqMrJk0')

@bot.message_handler(commands=['start','help'])
def start(message):
    mess = (f"Hello {message.from_user.first_name} {message.from_user.last_name}")
    bot.send_message(message.chat.id, mess , parse_mode='html')

@bot.message_handler(commands=['status'])
def start(message):
    ourOs = os.uname()
    bot.send_message(message.chat.id, ourOs, parse_mode='html')

# @bot.message_handler()
# def start(message):
#     bot.send_message(message.chat.id, message, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "Добрий день, ми з України!" , parse_mode='html')
    elif message.text == "document":
        document = open('/share/wpscan-output.txt', 'rb')
        bot.send_document(message.chat.id, document)
    else:
        bot.send_message(message.chat.id, "Зовсім баба не чує" , parse_mode='html')
        

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, "Дуже добре!")


# @bot.message_handler(content_types=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("Open web site", url="https://tproger.ru/articles/telegram-bot-create-and-deploy/"))
#     bot.send_message(message.chat.id, "Check the page", reply_markup=markup)



bot.polling(non_stop=True)