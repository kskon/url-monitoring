from celery import Celery
from datetime import datetime
import requests
from via_pony import adding_data

app = Celery('tasks')
app.config_from_object('celeryconfig')

@app.task
def urls(u):
    try:
        r = requests.get(u)
        result = (r.status_code == requests.codes.ok)
    except Exception:
        result = False
    finally:
        print (u, result)
        adding_data (u, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result)
