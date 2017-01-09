from celery import Celery
import datetime
import requests
from pony.orm import *

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
        #    put_in_db(u, result, str(datetime.datetime.now()))

'''
def put_in_db(url, result, date):
    try:
        conn = psycopg2.connect("dbname='py_monitor' user='python' host='localhost' password='123'")
        print ('connected succesfully')
        cur = conn.cursor()
        cur.execute("insert into test.gathering_data (res_addr, time, is_online) values (%s, %s, %s')", (url, date, result))
        conn.commit()
        cur.close()
        conn.close()
    except:
        print ("I am unable to connect to the database")

#urls(
'''
