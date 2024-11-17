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
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            title = soup.find('h1')
            if title is None:
                print(f"Заголовок не найден для ссылки: {link}")
                continue

            article_section = soup.find('article')
            if article_section:
                articles = article_section.find_all('p')
            else:
                articles = soup.find_all('p')

            content = [article.text.strip() for article in articles]

            with get_db() as db:
                new_news = News(title=title.text.strip(), link=link, articles='\n'.join(content))
                db.add(new_news)
                db.commit()
                db.refresh(new_news)

                print(f'Новость "{new_news.title}" сохранена в базу данных.')
        except requests.exceptions.RequestException as e:
            print(f'Ошибка загрузки страницы {link}: {e}')
        except IntegrityError:
            print(f'Новость с ссылкой "{link}" уже существует.')
            continue
        except Exception as e:
            print(f'Непредвиденная ошибка при обработке ссылки {link}: {e}')