from сontrollers.lenta.parsLinks import parsingNewsLinks
from сontrollers.lenta.parsNews import parsNews


def lenta_pars_task():
    links = parsingNewsLinks()
    parsNews(links)