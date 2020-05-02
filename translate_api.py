import requests

API_KEY = 'NTZlYWY4ZmQtNTViYy00ODk1LTljZjktMTg1OTk3NDA2YzAyOjJmNDEyNDE2NmQ4NzRkOTc4YjA0MDdhNjk0ODA4NTU2'
URL_API = 'https://developers.lingvolive.com/api/'
URL_AUTH = URL_API + 'v1.1/authenticate'
URL_TRANSLATE = URL_API + 'v1/Minicard'


def auth():
    headers = {
        'Authorization': 'Basic ' + API_KEY
    }
    response = requests.post(URL_AUTH, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception('Authenticate error')


def translate_en_ru(word):
    headers = {
        'Authorization': 'Bearer ' + token
    }
    params = {
        'text': word,
        'srcLang': 1033,
        'dstLang': 1049
    }
    response = requests.get(URL_TRANSLATE, params=params, headers=headers)
    #print(response.status_code)
    try:
        res = response.json()
        print(res['Translation']['Translation'])
        print('')
    except:
        print('Не найден перевод для слова')


token = auth()
while True:
    en_word = input('''Введите английское слово для перевода,
или q для выхода: ''')
    if en_word == 'q':
        break
    translate_en_ru(en_word)
