import psycopg2
import sqlite3

# create a sqlite db
sqliteConnection = sqlite3.connect('C:\\Users\dlebedev\PycharmProjects\AnimalTreeDjango\species.db')
sqliteCursor = sqliteConnection.cursor()
# ref: http://hakanu.net/sql/2015/08/25/sqlite-unicode-string-problem/
sqliteConnection.text_factory = lambda x: str(x, 'utf-8', 'ignore')

# connect to postgresql
pgConnectString = "port='5432' host='192.168.3.23' dbname='lifetree' user='postgres' password='postgres'"
pgConnection=psycopg2.connect(pgConnectString)
pgCursor = pgConnection.cursor()

# select from the table
pgCursor.execute("SELECT id, title, list_url from public.kingdoms")
rows = pgCursor.fetchall()

# loop and insert into sqlite
sqliteCursor.execute("delete from main.kingdoms")
for row in rows:
    sqliteCursor.execute("INSERT INTO main.kingdoms (id, title, list_url) VALUES (:id, :title, :list_url)", {'id':row[0], 'title':row[1], 'list_url':str(row[2])})
    sqliteConnection.commit()

# close all connections
sqliteConnection.close()
pgConnection.close()