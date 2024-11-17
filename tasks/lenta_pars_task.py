from сontrollers.parsLinks import parsingNewsLinks
from сontrollers.parsNews import parsNews


def lenta_pars_task():
    links = parsingNewsLinks('https://lenta.ru')
    parsNews(links)