import requests
from bs4 import BeautifulSoup
from settings.database_settings import get_db
from models.news_model import News
from sqlalchemy.exc import IntegrityError


def parsNews(links):
    # Парсим новости
    for link in links:
        try:
            response = requests.get(link)
            response.encoding = 'utf-8'

            soup = BeautifulSoup(response.text, 'html.parser')

            title = soup.find('h1')
            if title is None:
                print(f"Заголовок не найден для ссылки: {link}")
                continue

            articles = soup.find_all('p') 
            content = []

            for article in articles:
                content.append(article.text.strip()) 

            with get_db() as db:
                new_news = News(title=title.text.strip(), link=link, articles='\n'.join(content))
                db.add(new_news)
                db.commit()
                db.refresh(new_news)

                print(f'Новость "{new_news.title}" сохранена в базу данных.')
        except IntegrityError as error:
            print(f'Ошибка добавления новости с ссылкой "{link}": Дубликат. {error}')