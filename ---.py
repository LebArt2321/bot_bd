import csv, sqlite3

sqlite_connection = sqlite3.connect('final.db')
cursor = sqlite_connection.cursor()

with open('final.csv','r') as fin:
    dr = csv.DictReader(fin, delimiter=";")
    to_db = [(i['id'], i['name']) for i in dr]

cursor.executemany("INSERT or IGNORE INTO main (id, name) VALUES (?, ?);", to_db)
sqlite_connection.commit()
sqlite_connection.close()


