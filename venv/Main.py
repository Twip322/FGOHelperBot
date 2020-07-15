import telebot
import botconfig
import requests

bot=telebot.TeleBot(botconfig.TOKEN)
url='https://gamepress.gg/grandorder/materials'


@bot.message_handler(commands=['start'])
def start_reply(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}, последний Мастер Халдеи! Я Система Поддержки Сбора Ресурсов в Сингулярностях и Лостбелтах или СПСРвСиЛ, хотя, это не важно".format(
                         message.from_user))

@bot.message_handler(commands=['help'])
def help_reply(message):
    bot.send_message(message.chat.id, "В моей системе есть несколько команд:\n"
                     +"/materials (имя_материала)-Ищет места нахождения указанного материала\n"
                     +"/gacha -Позволяет перейти к симулятору призыва слуг")

@bot.message_handler(commands=['materials'])
def material_reply(message):
    to = message.text.replace('/materials ','').lower().replace(' ', '-')
    if (requests.get(f'https://gamepress.gg/grandorder/item/{to}').ok):
        bot.send_message(message.chat.id,
                         'О, я знаю несколько спотов!\n' + f'https://gamepress.gg/grandorder/item/{to}')
    else:
        bot.send_message(message.chat.id,
                         'Ой, кажется, я не знаю такого материала!\n Если что, можете найти необходимый ресурс здесь: '
                         + 'https://gamepress.gg/grandorder/materials')

@bot.message_handler(commands=['gacha'])
def toGacha_reply(message):
    bot.send_message(message.chat.id,'Оу, симулятор призыва? Хочешь потренироваться перед настоящим испытанием? Тогда тебе сюда: '
                     +'https://gamepress.gg/grandorder/summon-simulator')

@bot.message_handler(content_types=['text'])
def text_reply(message):
    bot.send_message(message.chat.id,'Моя система не предназначена для простых разговоров или внештатных команд, но так хотелось бы')

bot.polling(none_stop=True)

