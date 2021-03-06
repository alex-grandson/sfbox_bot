import config
import bot_answers
import telebot
import requests
import manager

bot = telebot.TeleBot(config.Token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
def handle_text_doc(message):
    file_info = bot.get_file(message.document.file_id)
    request = requests.get(f'https://api.telegram.org/file/bot{config.Token}/{file_info.file_path}')
    bot.reply_to(message, "Working...")
    manager.make_input_file(message.from_user.id, request.text)
    manager.start_sfbox(message.from_user.id)
    doc = open(f'{message.from_user.id}.out', 'rb')
    bot.send_document(message.chat_id, doc)


# sendDocument
# doc = open('/tmp/file.txt', 'rb')
# bot.send_document(chat_id, doc)

# tb.send_document(chat_id, "FILEID")

bot.polling(none_stop=True)
