import time
import requests

def decorat(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Время выполнения: {end-start} сек.')
    return wrapper

@decorat
def fetch_webpage():
    webpage = requests.get('https://ya.ru')

fetch_webpage()