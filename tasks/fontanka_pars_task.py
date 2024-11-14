from сontrollers.fontanka.parsLinks import parsingNewsLinks
from сontrollers.fontanka.parsNews import parsNews


def fontanka_pars_task():
    links = parsingNewsLinks()
    parsNews(links)