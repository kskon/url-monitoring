from pony.orm import *

db = Database()
db.bind('postgres', user='python', password='123', host='localhost', database='py_monitor')

class Gath_data(db.Entity):
    id = PrimaryKey(int, auto=True)
    addr = Required(str)
    time = Required(str)
    online = Required(bool)

db.generate_mapping(create_tables=True)

sql_debug(True)

#p1 = Gath_data(addr='http://www.google.ru', time='21:00', online=True)
#commit()

@db_session
def adding_data(addr, time, online):
    Gath_data(addr=addr, time=time, online=online)
    
p1 = adding_data('http://www.google.ru', '21:00', True)
