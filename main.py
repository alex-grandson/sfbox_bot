import config
import bot_answers
import telebot

bot = telebot.TeleBot(config.Token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, bot_answers.greetings(message.from_user.first_name))


@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
    print("yes")


bot.polling()
