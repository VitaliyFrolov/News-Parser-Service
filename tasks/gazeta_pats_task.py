from сontrollers.parsLinks import parsingNewsLinks
from сontrollers.parsNews import parsNews


def gazeta_pats_task():
    links = parsingNewsLinks('https://www.gazeta.ru')
    parsNews(links)