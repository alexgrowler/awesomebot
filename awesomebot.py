import telebot
import os
import psycopg2
DATABASE_URL = os.environ['postgres://vvpkyslecfulbd:b2268edcd9e36f9d844d139d6fda4c10c6085c43b391d1d20fb44ecee94c9126@ec2-54-163-245-64.compute-1.amazonaws.com:5432/d9euj24l5r9ud5']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')


bot = telebot.TeleBot("696871290:AAHjTGJQwyx6pm4qz5eJinAfxsaP_OefkIU")

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)