import telebot


#connect to sql
#import os
#import psycopg2
#DATABASE_URL = os.environ['postgres://vvpkyslecfulbd:b2268edcd9e36f9d844d139d6fda4c10c6085c43b391d1d20fb44ecee94c9126@ec2-54-163-245-64.compute-1.amazonaws.com:5432/d9euj24l5r9ud5']
#conn = psycopg2.connect(DATABASE_URL, sslmode='require')
#cursor = conn.cursor()
#cursor.execute("""CREATE TABLE tutorials (name char(40));""")
#cursor.execute("""SELECT * from tutorials""")
  #  rows = cursor.fetchall()
 #   print(rows)
#except Exception as e:
   # print("Uh oh, can't connect. Invalid dbname, user or password?")
  #  print(e)


#connect_str = "dbname='d9euj24l5r9ud5' user='vvpkyslecfulbd' host='ec2-54-163-245-64.compute-1.amazonaws.com' " + \
 #                 "password='b2268edcd9e36f9d844d139d6fda4c10c6085c43b391d1d20fb44ecee94c9126'"



#echo bot
bot = telebot.TeleBot("696871290:AAHjTGJQwyx6pm4qz5eJinAfxsaP_OefkIU")
#@bot.message_handler(content_types=['text'])
#def echo(message):
 #   bot.send_message(message.chat.id, message.text)



@bot.message_handler(commands=['ask'])





def mychat(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboarButton('Click here', callback_data='button_yes'))
    keyboard.row(telebot.types.InlineKeyboarButton('Click not here', callback_data='button_no'))
    bot.send_message(message.chat.id, 'Hi click any button!', reply_markup=keyboard)
     
#@bot.callback_query_handler(func = lambda call: call.data == 'button_yes')
#def newbutton (query):
 #   bot.edit_message_text(chat_id = query.message.chat.id,
  #                        message_id= query.message.message_id,
   #                       text='Yes!')

#@bot.callback_query_handler(func = lambda call: call.data == 'button_no')
#def newbutton (query):
 #   bot.edit_message_text(chat_id = query.message.chat.id,
  #                        message_id= query.message.message_id,
   #                       text='No!')

#def b(message):
 #   bot.send_message(message.chat.id, 'Your chat id: ' + str(message.chat.id))

    











if __name__ == '__main__':
    bot.polling(none_stop=True)