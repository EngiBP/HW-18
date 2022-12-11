import telebot
from token import TOKEN
from extensions import ConvertionException, CryptoConverter

TOKEN = "5640808594:AAGTPLY0YipY5aNj_PorCJn6oQ7hD-heYbs"

bot = telebot.TeleBot(TOKEN)

keys = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}

@bot.message_handler(commands = ['start'])
def handler_start(message: telebot.types.Message):
    text = f'Доброго времени суток, {message.chat.username}!\n' \
           'Меня зовут Men9iJlaBot и я ваш помошник в конвертации валют:\n' \
           'Список доступных валют вы можете посмотреть с помощью команды /values ;\n' \
           'Для того чтобы произвести конвертацию ввидете данные в следующем формате:\n' \
           '<Наименование переводимой валюты> <Наименование валюты в которую перевести> <сумма>;\n' \
           'Если вам что то не понятно попросите помощи командой /help'
    bot.reply_to(message, text)

@bot.message_handler(commands = ['help'])
def handler_help(message: telebot.types.Message):
    text = 'Для того чтобы произвести конвертацию введите данные в следующем формате:\n' \
           '<Наименование переводимой валюты> <Наименование валюты в которую перевести> <сумма>\n' \
           'Для просмотра списка доступных валют воспользуйтесь командой /values'
    bot.reply_to(message, text)

@bot.message_handler(commands = ['values'])
def handler_values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types = ['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
             raise ConvertionException('Слишком много параметров.')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователяю\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} = {total_base}'
        bot.send_message(message.chat.id, text)

bot.polling(none_stop = True)