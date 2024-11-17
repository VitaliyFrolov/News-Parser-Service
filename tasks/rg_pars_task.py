from сontrollers.parsLinks import parsingNewsLinks
from сontrollers.parsNews import parsNews


def rg_pars_task():
    links = parsingNewsLinks('https://rg.ru')
    parsNews(links)