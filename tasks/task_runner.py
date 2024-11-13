import threading
import schedule
import time
from tasks.pars_task import pars_task


schedule.every().day.at('100:00').do(pars_task)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    thread = threading.Thread(target=run_scheduler)
    thread.start()