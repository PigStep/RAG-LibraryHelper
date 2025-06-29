import requests
from bs4 import BeautifulSoup

def parse_html_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Ошибка: {response.status_code}")

