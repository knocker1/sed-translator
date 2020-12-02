import urllib3
import urllib.parse
import json

import config

key = config.yandex_token

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()

def translate(lang, text):
    lang = lang
    text = urllib.parse.quote_plus(text)
    response = http.request('GET', 'https://translate.yandex.net/api/v1.5/tr.json/translate?' + 'key=' + key + '&lang=' + lang + '&text=' + text)
    response_decode = response.data.decode("utf-8")
    result = json.loads(response_decode)['text']
    return result[0]



