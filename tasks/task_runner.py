import threading
import schedule
import time
from tasks.fontanka_pars_task import fontanka_pars_task
from tasks.lenta_pars_task import lenta_pars_task


schedule.every().day.at('10:00').do(fontanka_pars_task)
schedule.every().day.at('10:10').do(lenta_pars_task)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    thread = threading.Thread(target=run_scheduler)
    thread.start()