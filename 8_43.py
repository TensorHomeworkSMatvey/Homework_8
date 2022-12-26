import time
import requests

def decorat(func):
    def wrapper():
        time.sleep(1)
        func()
    return wrapper

@decorat
def fetch_webpage():
    webpage = requests.get('https://ya.ru')

fetch_webpage()