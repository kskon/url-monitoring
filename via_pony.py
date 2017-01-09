from pony.orm import *


class Gath_data(db.Entity):
    id = PrimaryKey(int, auto=True)
    addr = Required(str)
    time = Required(str)
    online = Required(bool)


@db_session
def adding_data(addr, time, online):
    Gath_data(addr=addr, time=time, online=online)

db = Database()
db.bind('postgres', user='python', password='123', host='localhost', database='py_monitor')
db.generate_mapping(create_tables=True)
sql_debug(True)
