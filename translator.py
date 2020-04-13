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
    user_file = input('Введите название файла: ')
    with open(user_file + '.txt', 'r', encoding="utf-8" ) as new_file:
        new_file_read = new_file.read().strip()
        new_file_output = open('resalt/' + user_file + '_output.txt', "w", encoding = 'utf-8')
        new_file_output.write(translate_it(new_file_read))
        new_file_output.close()
    print(f"Запись в файл завершена, файл {new_file_output} сохранен")

