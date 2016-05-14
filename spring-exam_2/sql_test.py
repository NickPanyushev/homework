#!/bin/python3

import sqlite3 as sql

query = "create table Users (" \
        "id integer primary key autoincrement, --user id" \
        "username text unique not null, --username," \
        "registered datetime not null --when user" \
        "--registered" \
        ");"

with sql.connect("data.sqlite") as data:  # открыли соединение с базой данных
    cur = data.cursor()  # получили курсор
    # for row in cur.execute(
    #     "create table Artists (" \
    #     "id integer primary key autoincrement, --artist id" \
    #     "name text unique not null, --name," \
    #     ");"):
    #     print (row)
    select * from Albums limit 3

def unpaid(user_id):
    with sql.connect("data.sqlite") as db:
        cur = db.cursor()
        data = cur.execute(query).fetchall()


    return data

print()