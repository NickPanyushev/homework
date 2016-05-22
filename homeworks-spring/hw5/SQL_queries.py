import sqlite3

db = sqlite3.connect('data.sqlite')
cursor = db.cursor()

t = cursor.execute('select * from Goods limit 5').fetchall()
