import requests


API_KEY = 'trnsl.1.1.20200410T144441Z.c3da493037e85651.17141e8c1c1797ed89379865149d7492889ccc11'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    """
    params = {
        'key': API_KEY,
        'text': text,
        'lang': 'ru',
        'options': '1', # автомотическое определение переводимого языка 
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])

if __name__ == '__main__':
    with open('DE.txt', 'r', encoding="utf-8") as DE:
        DE_read = DE.read().strip()
        DE_output = open("resalt\DE_output.txt", "w", encoding = 'utf-8')
        DE_output.write(translate_it(DE_read))
        DE_output.close()

    with open('ES.txt', 'r', encoding="utf-8") as ES:
        ES_read = ES.read().strip()
        ES_output = open("resalt\ES_output.txt", "w", encoding = 'utf-8')
        ES_output.write(translate_it(ES_read))
        ES_output.close()

    with open('FR.txt', 'r', encoding="utf-8") as FR:
        FR_read = FR.read().strip()
        FR_output = open("resalt\FR_output.txt", "w", encoding = 'utf-8')
        FR_output.write(translate_it(FR_read))
        FR_output.close()

