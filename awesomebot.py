# на коменты обрати внимание, пиши звони с вопросами


import telebot
from pymongo import MongoClient

token = '696871290:AAHjTGJQwyx6pm4qz5eJinAfxsaP_OefkIU'
bot = telebot.TeleBot(token, threaded = False)

#подключение к БД
mongourl = 'mongodb://heroku_rffktvp8:jde852odv8uevo2an1ms8cdfq1@ds131763.mlab.com:31763/heroku_rffktvp8'
client = MongoClient(mongourl)
db = client['heroku_rffktvp8']
botdb = db.mydb


# запись в бд.Ключевой параметр, вызывающий функцию "end". Функция должна вызываться после показа КР-кода. сейчас они вписана в первую функцию: строки 257-258.
@bot.callback_query_handler(func=lambda call: call.data == 'end')
def jjjjj(query):
    if botdb.find({'chat_id': query.message.chat.id}).count() == 0:
        data = {
            'chat_id': query.message.chat.id#,
            #'type': type1
            }
        botdb.insert_one(data)
    else:
        pass
#    botdb.update_one({'chat_id': query.message.chat.id},
#                    {'$set':{
#                        'type': 'Granola',
#                        'name': 'Name'
#                    }})

#здесь переменные-вопросы


#здесь переменные-ответы


#начало работы с юзером
@bot.message_handler(commands=['start'])
def sphere(message):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('Кафе', callback_data='cafe'))
    keyboard1.row(telebot.types.InlineKeyboardButton('Бар', callback_data='bar'))
    keyboard1.row(telebot.types.InlineKeyboardButton('Ресторан', callback_data='restaurant'))
    create1 = bot.send_message(message.chat.id, '*Выберите тип заведение, которое вы посетили:*',
                               reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'cafe')
def cafe(query):
    type1 = 'cafe'
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('Granola', callback_data='gran'))
    keyboard1.row(telebot.types.InlineKeyboardButton('Mouse Tail', callback_data='mouse'))
    bot.edit_message_text(chat_id=query.message.chat.id,
                          message_id=query.message.message_id,
                          text='*Какое кафе вы посетили?*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'bar')
def bar(query):
    type1 = 'bar' #
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('Techno', callback_data='tech'))
    keyboard1.row(telebot.types.InlineKeyboardButton('1703', callback_data='numb'))
    bot.edit_message_text(chat_id=query.message.chat.id,
                          message_id=query.message.message_id,
                          text='*Какой бар вы посетили?*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'restaurant')
def restaurant(query):
    type1 = 'restaraunt'
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('Palkin', callback_data='pal'))
    keyboard1.row(telebot.types.InlineKeyboardButton('Woody', callback_data='woo'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Какой ресторан вы посетили?*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'gran')
def gran(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('Мужчина', callback_data='m1'))
    keyboard1.row(telebot.types.InlineKeyboardButton('Женщина', callback_data='f1'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш пол:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'mouse')
def mouse (query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('Мужчина', callback_data='m2'))
    keyboard1.row(telebot.types.InlineKeyboardButton('Женщина', callback_data='f2'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш пол:*', reply_markup=keyboard1, parse_mode='markdown')



@bot.callback_query_handler(func=lambda call: call.data == 'tech')
def tech (query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('Мужчина', callback_data='ma1'))
    keyboard1.row(telebot.types.InlineKeyboardButton('Женщина', callback_data='fe1'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш пол:*', reply_markup=keyboard1, parse_mode='markdown')

@bot.callback_query_handler(func=lambda call: call.data == 'numb')
def numb(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('Мужчина', callback_data='ma2'))
    keyboard1.row(telebot.types.InlineKeyboardButton('Женщина', callback_data='fe2'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш пол:*', reply_markup=keyboard1, parse_mode='markdown')

@bot.callback_query_handler(func=lambda call: call.data == 'pal')
def pal (query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('Мужчина', callback_data='mal1'))
    keyboard1.row(telebot.types.InlineKeyboardButton('Женщина', callback_data='fem1'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш пол:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'woo')
def woo(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('Мужчина', callback_data='mal2'))
    keyboard1.row(telebot.types.InlineKeyboardButton('Женщина', callback_data='fem2'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш пол:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'm1')
def m1(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('до 25', callback_data='a11'))
    keyboard1.row(telebot.types.InlineKeyboardButton('26-45', callback_data='a22'))
    keyboard1.row(telebot.types.InlineKeyboardButton('больше 45', callback_data='a33'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш возраст:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'm2')
def m2(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('до 25', callback_data='b11'))
    keyboard1.row(telebot.types.InlineKeyboardButton('26-45', callback_data='b22'))
    keyboard1.row(telebot.types.InlineKeyboardButton('больше 45', callback_data='b33'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш возраст:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'f1')
def f1(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('до 25', callback_data='c11'))
    keyboard1.row(telebot.types.InlineKeyboardButton('26-45', callback_data='c22'))
    keyboard1.row(telebot.types.InlineKeyboardButton('больше 45', callback_data='c33'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш возраст:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'f2')
def f2(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('до 25', callback_data='aa11'))
    keyboard1.row(telebot.types.InlineKeyboardButton('26-45', callback_data='aa22'))
    keyboard1.row(telebot.types.InlineKeyboardButton('больше 45', callback_data='aa33'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш возраст:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'ma1')
def ma1(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('до 25', callback_data='bb11'))
    keyboard1.row(telebot.types.InlineKeyboardButton('26-45', callback_data='bb22'))
    keyboard1.row(telebot.types.InlineKeyboardButton('больше 45', callback_data='bb33'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш возраст:*', reply_markup=keyboard1, parse_mode='markdown')

@bot.callback_query_handler(func=lambda call: call.data == 'fe1')
def fe1(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('до 25', callback_data='cc11'))
    keyboard1.row(telebot.types.InlineKeyboardButton('26-45', callback_data='cc22'))
    keyboard1.row(telebot.types.InlineKeyboardButton('больше 45', callback_data='cc33'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш возраст:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'ma2')
def ma2(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('до 25', callback_data='aaa11'))
    keyboard1.row(telebot.types.InlineKeyboardButton('26-45', callback_data='aaa22'))
    keyboard1.row(telebot.types.InlineKeyboardButton('больше 45', callback_data='aaa33'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш возраст:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'fe2')
def fe2(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('до 25', callback_data='bbb11'))
    keyboard1.row(telebot.types.InlineKeyboardButton('26-45', callback_data='bbb22'))
    keyboard1.row(telebot.types.InlineKeyboardButton('больше 45', callback_data='bbb33'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш возраст:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'mal1')
def mal1(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('до 25', callback_data='ccc11'))
    keyboard1.row(telebot.types.InlineKeyboardButton('26-45', callback_data='ccc22'))
    keyboard1.row(telebot.types.InlineKeyboardButton('больше 45', callback_data='ccc33'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш возраст:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'mal2')
def mal2(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('до 25', callback_data='aaa111'))
    keyboard1.row(telebot.types.InlineKeyboardButton('26-45', callback_data='aaa222'))
    keyboard1.row(telebot.types.InlineKeyboardButton('больше 45', callback_data='aaa333'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш возраст:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'fem1')
def fem1(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('до 25', callback_data='bbb111'))
    keyboard1.row(telebot.types.InlineKeyboardButton('26-45', callback_data='bbb222'))
    keyboard1.row(telebot.types.InlineKeyboardButton('больше 45', callback_data='bbb333'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш возраст:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'fem2')
def fem2(query):
    keyboard1 = telebot.types.InlineKeyboardMarkup()
    keyboard1.row(telebot.types.InlineKeyboardButton('до 25', callback_data='ccc111'))
    keyboard1.row(telebot.types.InlineKeyboardButton('26-45', callback_data='ccc222'))
    keyboard1.row(telebot.types.InlineKeyboardButton('больше 45', callback_data='ccc333'))
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text='*Укажите Ваш возраст:*', reply_markup=keyboard1, parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'a11')
def a11(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown') #нужно вставить callback_data='end' для проверки ф-ии БД, прим. ниже
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'a22')
def a22(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('26-45')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'a33')
def a33(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('>45')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'aa11')
def aa11(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'aa22')
def aa22(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'aa33')
def aa33(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'aaa11')
def aaa11(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'aaa22')
def aaa22(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'aaa33')
def aaa33(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'aaa111')
def aaa111(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'aaa222')
def aaa222(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'aaa333')
def aaa333(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'b11')
def b11(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)
    
@bot.callback_query_handler(func=lambda call: call.data == 'b22')
def b22(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'b33')
def b33(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'bb11')
def bb11(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'bb22')
def bb22(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'bb33')
def bb33(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'bbb11')
def bbb11(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'bbb22')
def bbb22(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'bbb33')
def bbb33(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'bbb111')
def bbb111(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'bbb222')
def bbb222(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'bbb333')
def bbb333(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'c11')
def c11(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'c22')
def c22(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'c33')
def c33(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'cc11')
def cc11(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'cc22')
def cc22(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')
    data = {'chat_id': str(query.message.chat.id),
            'type': str('cafe'),
            'name': str('Granola'),
            'gender': str('male'),
            'age': str('<25')
            } 
    botdb.insert_one(data)

@bot.callback_query_handler(func=lambda call: call.data == 'cc33')
def cc33(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')

@bot.callback_query_handler(func=lambda call: call.data == 'ccc11')
def ccc11(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'ccc22')
def ccc22(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'ccc33')
def ccc33(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'ccc111')
def ccc11(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'ccc222')
def ccc222(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'ccc333')
def ccc333(query):
    finalvars = '[Покажите полученный QR-code в заведении при следующем визите:](https://img.icons8.com/metro/1600/qr-code.png)'
    bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                          text= finalvars + '\n*Айди пользователя: *' + str(query.message.chat.id), parse_mode='markdown')

    for text in finalvars:
        bot.send_message(query.message.chat.id, text, parse_mode='markdown')




#@bot.message_handler(commands=['start', 'help'])
#def handle_start_help(message):
 #   pass

#bot.polling(none_stop=True, interval=0)

#import sqlite3

#connection = sqlite3.connect("database", check_same_thread = True)
#cursor = connection.cursor()

#cursor.execute("CREATE TABLE IF NOT EXISTS Inventory_on (ID INT, 'Primary weapon' TEXT, 'Secondary weapon' TEXT)")
#cursor.execute("CREATE TABLE IF NOT EXISTS Clans (Name TEXT, Points INT)")
#cursor.execute("CREATE TABLE IF NOT EXISTS WorkStatus (ID INT, Status INT)")

#connection.commit()
#connection.close()

if __name__ == '__main__':
    bot.polling(none_stop=True)