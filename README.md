# News Parser Service

## Данный сервис был реализован в рамках проекта News Aggregator

### Данный сервис предпологает наличие базы данных с созданной таблицей news*
## Функционал:
1. Парсинг новостных сайтов
2. Сохранение полученных новостей в базу данных

## Стек:
- FastAPI + BeautifulSoup4
- Python
- Venv
- Schedule
- Pg + SQLAlchemy
- Docker
- Uvicorn

### Список новостных сайтов:
- https://www.fontanka.ru
- https://lenta.ru

## Для сборки проекта:
- `make build`