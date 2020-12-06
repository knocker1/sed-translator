import telebot
from telebot import types
import config
import translator as tr
import database as db
import asyncio


bot = telebot.TeleBot(config.telegram_token)


@bot.message_handler(commands=['start'])
def start_bot(message):
    chat_type = message.chat.type
    if chat_type != "private":      
        admin_list = bot.get_chat_administrators(message.chat.id)
        if message.from_user.id not in admin_list:
             return
    else:
        pass
    if db.user_exist(message.chat.id):
        bot.send_message(message.chat.id, 'You have already started a conversation with this bot.\n'
                                          'Use to view a list of all commands '
                                          'command - /help.')
    else:
        user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                one_time_keyboard=True)
        sorted_langs = sorted(db.top_langs.items(), key=lambda kv: kv[1])
        for lang in sorted_langs:
            user_markup.row(lang[1])
        msg = bot.send_message(message.chat.id,
                         'This is a bot, that'
                         'built on Yandex-translator and supports over '
                         '90 languages of the world. \nNow over to you '
                         'you must specify the language into which the text will be translated. '
                         '\nYou can change the translation language using the command '
                         '/langs (all languages) and /top_langs (the most popular languages). '
                         '\nThe language of the input text is determined automatically. '
                         '\nYou can view a list of all commands in the commands menu, '
                         'next to the send key.', reply_markup=user_markup)

        def add_user(msg):
            usr_lang = msg.text
            db.add_user(msg.chat.id, usr_lang)
            hide_markup = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, 'Perfect!', reply_markup=hide_markup)


        bot.register_next_step_handler(msg, add_user)

@bot.message_handler(commands=['langs'])
def change_langs(message):
    chat_type = message.chat.type
    if chat_type != "private":      
        admin_list = bot.get_chat_administrators(message.chat.id)
        if message.from_user.id not in admin_list:
             return
    else:
        pass
    user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                            one_time_keyboard=True)
    sorted_langs = sorted(db.langs.items(), key=lambda kv: kv[1])
    for lang in sorted_langs:
        user_markup.row(lang[1])
    msg = bot.send_message(message.chat.id,
                           'Please select a new language to translate:',
                           reply_markup=user_markup)
    def change(msg):
        usr_lang = msg.text
        db.change_langs(msg.chat.id, usr_lang)
        hide_markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Language changed successfully!',
                         reply_markup=hide_markup)

    bot.register_next_step_handler(msg, change)

@bot.message_handler(commands=['top_langs'])
def change_langs(message):
    chat_type = message.chat.type
    if chat_type != "private":      
        admin_list = bot.get_chat_administrators(message.chat.id)
        if message.from_user.id not in admin_list:
             return
    else:
        pass
    user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                            one_time_keyboard=True)
    sorted_langs = sorted(db.top_langs.items(), key=lambda kv: kv[1])
    for lang in sorted_langs:
        user_markup.row(lang[1])
    msg = bot.send_message(message.chat.id,
                           'Please select a new language to translate:',
                           reply_markup=user_markup)

    def change(msg):
        usr_lang = msg.text
        db.change_top_langs(msg.chat.id, usr_lang)
        hide_markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Language changed successfully!',
                         reply_markup=hide_markup)

    bot.register_next_step_handler(msg, change)

#@bot.message_handler(commands=['about'])
#def about(message):
 #   bot.send_message(message.chat.id, 'My name is Ostap. '
 
@bot.message_handler(content_types=['text'])
def translate_text(message):
    chat_type = message.chat.type
    if chat_type != "private":      
        admin_list = bot.get_chat_administrators(message.chat.id)
        if message.from_user.id not in admin_list:
             return
    else:
        pass
    usr_lang = db.users_data[str(message.chat.id)]
    if len(message.text) >= 4050:
        bot.send_message(message.chat.id,
                         'Text length should not exceed 4050 characters.')
    else:
        try:
            transl_response = tr.translate(usr_lang, message.text)
            bot.send_message(message.chat.id, transl_response)
        except:
            bot.send_message(message.chat.id,
                             'Text length is too long.')

if __name__ == '__main__':
    bot.polling(none_stop=True)
