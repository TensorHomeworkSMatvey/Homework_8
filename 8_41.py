import requests

def decorat(func):
    def wrapper():
        func()
        print("Функция отработала без ошибок")
    return wrapper

@decorat
def fetch_webpage():
    webpage = requests.get('https://ya.ru')

fetch_webpage()