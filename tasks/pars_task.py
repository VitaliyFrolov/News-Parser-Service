from сontrollers.parsLinks import parsingNewsLinks
from сontrollers.parsNews import parsNews


def pars_task():
    links = parsingNewsLinks()
    parsNews(links)