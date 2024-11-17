import threading
import schedule
import time
#Task list
from tasks.fontanka_pars_task import fontanka_pars_task
from tasks.lenta_pars_task import lenta_pars_task
from tasks.rg_pars_task import rg_pars_task
from tasks.gazeta_pats_task import gazeta_pats_task


schedule.every().day.at('10:00').do(fontanka_pars_task)
schedule.every().day.at('10:20').do(lenta_pars_task)
schedule.every().day.at('10:30').do(rg_pars_task)
schedule.every().day.at('10:40').do(gazeta_pats_task)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    thread = threading.Thread(target=run_scheduler)
    thread.start()