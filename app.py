import telebot
from config import keys, TOKEN
from extensions import CryptoConverter, APIExeption


bot = telebot.TeleBot(TOKEN)





@bot.message_handler(commands=['start','help'])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу, введите комманду боту в следующем формате:\n<имя валюты>   <в какую валюту перевести>   <количество переводимой валюты>\
    \nУвидеть список всех возможных валют: /values"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text='\n'.join((text,key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    text="Не удалось обработать команду!\nПричина: "
    try:
        values = message.text.split(' ')
        if len(values)>3:
            raise APIExeption('Слишком много параметров!')
        if len(values)<3:
            raise APIExeption('Слишком мало параметров!')
        quote, base, amount = values
        text = CryptoConverter.get_price(quote, base, amount)
    except Exception as e:
        text += str(e)
    finally:
        bot.send_message(message.chat.id, text)

bot.polling()