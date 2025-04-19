import psycopg2
import csv
from datetime import datetime

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="kaz130212",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

def insert_or_update_user(username, phone, birth_date):
    cursor.execute("CALL insert_or_update_user(%s, %s, %s);", (username, phone, birth_date))
    conn.commit()

def insert_many_users(usernames, phones, birth_dates):
    cursor.execute(
        "SELECT * FROM insert_many_users_arr(%s, %s, %s);",
        (usernames, phones, birth_dates)
    )
    invalids = cursor.fetchall()
    for user in invalids:
        print("Invalid:", user)

def search_users(pattern):
    cursor.execute("SELECT * FROM search_users(%s);", (pattern,))
    results = cursor.fetchall()
    for row in results:
        print(row)

def get_users_with_pagination(limit, offset):
    cursor.execute("SELECT * FROM get_users_with_pagination(%s, %s);", (limit, offset))
    for row in cursor.fetchall():
        print(row)

def delete_user(username=None, phone=None):
    cursor.execute("CALL delete_user(%s, %s);", (username, phone))
    conn.commit()

insert_or_update_user("Jan Clode", "82256189094", "1234-02-08")
