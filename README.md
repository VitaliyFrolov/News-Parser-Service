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
- https://www.gazeta.ru
- https://rg.ru

## Для сборки проекта:
- `make build`

После сборки проекта будет доступен сервис, который парсит новостные сайты, получает с них новости и кладет их в таблицу news, находящуюся в вашей базе данных.

Данный сервис был разработан в рамках проекта <b>News-Aggregator</b>
- [Client](https://github.com/VitaliyFrolov/News-Aggregator-Client)
- [API/Server](https://github.com/VitaliyFrolov/News-Aggregator-Server)
- News Parser Service