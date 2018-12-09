import telebot




bot = telebot.TeleBot("696871290:AAHjTGJQwyx6pm4qz5eJinAfxsaP_OefkIU")

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)