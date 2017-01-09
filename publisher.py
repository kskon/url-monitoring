import configparser
from time import sleep
from celery import group
from tasks import *
import datetime

config = configparser.ConfigParser()
config.read('cfg.cfg')
periodicity = config.getint('sect1', 'timing')
res_list = config['sect1']['urls'].split('\n')
try:
    res_list.remove('')
except Exception:
    pass

length = len(res_list)
app.conf.update(CELERYD_CONCURRENCY=length)
#app.conf.update(CELERYD_CONCURRENCY=4)
while True:
    res = group(urls.s(x) for x in res_list)()
    sleep(periodicity)
