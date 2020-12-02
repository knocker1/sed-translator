langs = {'cy': 'Welsh', 'tl': 'Tagal', 'sk': 'Slovak',
         'bg': 'Bulgarian', 'ml': 'Malayalam', 'sr': 'Serbian', 'jv': 'Javanese',
         'ar': 'Аrabic', 'mt': 'Maltese', 'tr': 'Turkish', 'tg': 'Tajik',
         'lo': 'Lao', 'id': 'Indonesian', 'pl': 'Polish',
         'az': 'Azerbaijani', 'el': 'Greek', 'ca': 'Catalan',
         'fa': 'Persian', 'cs': 'Czech', 'kn': 'Kannada', 'en': 'English',
         'mg': 'Malagasy', 'gl': 'Galician', 'my': 'Burmese',
         'la': 'Latin', 'uk': 'Ukrainian', 'ka': 'Georgian', 'ru': 'Russian',
         'no': 'Norwegian', 'si': 'Singal', 'pap': "Papiamento",
         'lv': 'Latvian', 'gu': 'Gujarati', 'bs': 'Bosnian',
         'mrj': 'Mountain Marian', 'ta': 'Tamil', 'ur': 'Urdu',
         'su': 'Sundanese', 'mk': 'Macedonian', 'ky': 'Киргизька (Kirgizka)',
         'pa': 'Punjabi', 'sv': 'Swedish', 'hu': 'Hungarian', 'ko': 'Korean',
         'zh': 'Chinese', 'sw': 'Swahili', 'eu': 'Basque',
         'nl': 'Dutch', 'he': 'Hebrew', 'udm': 'Udmurt',
         'ga': 'Irish', 'hy': 'Armenian', 'th': 'Thai', 'xh': 'Hair',
         'kk': 'Kazakh', 'lt': 'Lithuanian', 'af': 'Afrikaans',
         'tt': 'Tatar', 'ja': 'Japanese', 'ro': 'Romanian', 'de': 'German',
         'uz': 'Uzbek', 'sq': 'Albanian', 'it': 'Italian', 'fi': 'Finnish',
         'bn': 'Bengali', 'hr': 'Croatian', 'is': 'Icelandic',
         'mn': 'Mongolian', 'te': 'Telugu', 'mr': 'Marathi', 'ht': 'Haitian',
         'fr': 'French', 'eo': 'Esperanto', 'be': 'Belarusian', 'et': 'Estonian',
         'pt': 'Portuguese', 'mi': 'Maori', 'es': 'Spanish', 'da': 'Danish',
         'ceb': 'Cebuano', 'am': 'Amharic', 'ne': 'Nepali', 'ms': 'Malay',
         'ba': 'Bashkirska', 'sl': 'Slovenian', 'km': 'Khmer', 'mhr': 'Mariyska',
         'hi': 'Hindi', 'yi': 'Yiddish', 'lb': 'Luxembourgish', 'vi': "В'Vietnamese",
         'gd': 'Scottish (Gaelic)'}


top_langs = {'en': 'English', 'it': 'Italian', 'de': 'German',
             'fr': 'French', 'pl': 'Polish', 'es': 'Spanish',
             'uk': 'Ukrainian', 'ru': 'Russian', 'hi': 'Hindi'}

users_data = {}

def user_exist(chat_id):
    if str(chat_id) in users_data:
        return True
    else:
        return False

def add_user(chat_id, usr_lang):
    users_data[str(chat_id)] = \
        str(list(langs.keys())[list(langs.values()).index(str(usr_lang))])

def change_langs(chat_id, usr_lang):
    users_data[str(chat_id)] = \
        str(list(langs.keys())[list(langs.values()).index(str(usr_lang))])

def change_top_langs(chat_id, usr_lang):
    users_data[str(chat_id)] = \
        str(list(top_langs.keys())[list(top_langs.values()).index(str(usr_lang))])
