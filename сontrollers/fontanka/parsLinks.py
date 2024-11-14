import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re


def parsingNewsLinks():
    # Получаем все ссылки на новости с сайта фонтанки
    url = 'https://www.fontanka.ru'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []

    for link in soup.find_all('a', href=lambda href: href and re.search(r'/20[0-9]{2}/[0-9]{2}/[0-9]{2}/', href)):
        full_link = urljoin(url, link['href'])
        links.append(full_link)

    return links