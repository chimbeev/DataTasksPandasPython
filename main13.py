import sqlite3

base = sqlite3.connect('new.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS data(login, password)')
base.commit()

cur.execute('INSERT INTO data VALUES(?, ?)', ('JONNY123', '123456'))
base.commit()
