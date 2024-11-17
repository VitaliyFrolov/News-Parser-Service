from fastapi import FastAPI, APIRouter
from cors import setup_cors
from tasks.task_runner import start_scheduler
from settings.database_settings import *


app = FastAPI()
router = APIRouter()

setup_cors(app)

start_scheduler()