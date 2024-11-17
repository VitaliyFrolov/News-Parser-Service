import threading
import schedule
import time
from tasks.fontanka_pars_task import fontanka_pars_task
from tasks.lenta_pars_task import lenta_pars_task


schedule.every().day.at('18:40').do(fontanka_pars_task)
schedule.every().day.at('18:41').do(lenta_pars_task)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    thread = threading.Thread(target=run_scheduler)
    thread.start()