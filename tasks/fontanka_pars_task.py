from сontrollers.parsLinks import parsingNewsLinks
from сontrollers.parsNews import parsNews


def fontanka_pars_task():
    links = parsingNewsLinks('https://www.fontanka.ru')
    parsNews(links)