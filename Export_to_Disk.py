import requests
import yadisk


OAuth = 'AgAAAAA2KrloAAZH2Os8U637Wk-wu0AtbuMMFEk'
# URL = 'https://oauth.yandex.ru/verification_code'
ID = 'c586de03eb6f4f3ab25c741e8807429c'
Pass = 'd5246abae1f24edba996d9d096acaf9e'

y = yadisk.YaDisk(ID, Pass, OAuth)

user_file = input('Введите название файла: ')
with open('resalt/' + user_file + '.txt', "rb") as f:
    y.upload(f, user_file + '.txt') 
    print(y.get_files())