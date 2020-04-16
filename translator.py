import requests
import glob

API_KEY = 'trnsl.1.1.20200410T144441Z.c3da493037e85651.17141e8c1c1797ed89379865149d7492889ccc11'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(file_from, file_to, lng_from = ['de', 'es', 'fr'], lng_to = 'ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
        :return:
    """
    # file_from = glob.glob("*.txt")
    for name_1 in file_from:
        with open(name_1, 'r', encoding="utf-8") as text_file_1:
            tr = text_file_1.read().strip()

    params = {
            'key': API_KEY,
            'text' : tr,
            'lang': '{}-''{}'.format(lng_from, lng_to),
        }

    response = requests.get(URL, params=params)
    json_ = response.json()
    # return ''.join(json_.get('text'))
    # for tr in json_['text']:   
    for name_2 in file_to:
        with open(name_2, 'w', encoding="utf-8") as text_2:
            text_2.write(''.join(json_['text']))

if __name__ == '__main__':
    translate_it(glob.glob("DE.txt"), glob.glob("resalt/DE_output.txt"),'de', 'ru')
    translate_it(glob.glob("FR.txt"), glob.glob("resalt/FR_output.txt"),'fr', 'ru')
    translate_it(glob.glob("ES.txt"), glob.glob("resalt/ES_output.txt"),'es', 'ru')


