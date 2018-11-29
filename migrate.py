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
pgCursor.execute("SELECT id, kingdom_id, title, page_url, type, image_url, parent_id from public.list")
rows = pgCursor.fetchall()

# loop and insert into sqlite
sqliteCursor.execute("delete from main.list")
for row in rows:
    sqliteCursor.execute("INSERT INTO main.list (id, kingdom_id, title, page_url, type, image_url, parent_id) VALUES (:id, :kingdom_id, :title, :page_url, :type, :image_url, :parent_id)", {'id':row[0], 'kingdom_id':row[1], 'title':row[2], 'page_url':str(row[3]), 'type':row[4], 'image_url':str(row[5]), 'parent_id':row[6]})
    sqliteConnection.commit()

# close all connections
sqliteConnection.close()
pgConnection.close()