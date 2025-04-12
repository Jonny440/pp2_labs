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

def insert_from_list():
    global conn, cursor
    names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
    phones = ["123456789", "987654321", "555123456", "444555666", "111222333"]

    for i in range(0, min(len(names), len(phones))):
        db_insert(names[i], phones[i], None)

def db_insert(username, phone, birth_date):
    global conn, cursor
    cursor.execute("SELECT * FROM phonebook WHERE username = %s", (username, ))
    results = cursor.fetchall()
    if not results:
        #data type check
        if not phone.isdigit():
            print("Incorrect phone format")
            return
        try:
            date = datetime.strptime(birth_date, "%Y-%m-%d").date()
        except ValueError:
            print("Incorrect date format. Use YYYY-MM-DD")
            return
        cursor.execute("""
            INSERT INTO phonebook (username, phone, birth_date)
            VALUES (%s, %s, %s);""",
            (username, phone, birth_date))
    else: # update phone number if user exists
        cursor.execute("""
            UPDATE phonebook
            SET phone = %s
            WHERE username = %s""",
            (phone, username))
    conn.commit()

def console_input():
    global conn, cursor
    username = str(input("Enter name: "))
    phone = str(input("Enter phone(without spaces): "))
    birth_date = input("Enter birth date (YYYY-MM-DD): ")

    db_insert(username, phone, birth_date)
    print("Data inserted from console")

def csv_input(filename):
    global conn, cursor
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            db_insert(row['username'], row['phone'], row['birth_date'])
    print("Inserted from CSV")

def update_user():
    global conn, cursor
    field = input("Update 'username' or 'phone': ").strip().lower()
    if field not in ['username', 'phone']:
        print("Invalid field.")
        return

    identifier = input("Enter current username or phone to find the record: ")
    new_value = input(f"Enter new {field}: ")

    cursor.execute(f"""
        UPDATE phonebook
        SET {field} = %s
        WHERE username = %s OR phone = %s;
    """, (new_value, identifier, identifier))

    conn.commit()
    print("Updated successfully")

def print_query():
    global cursor
    results = cursor.fetchall()
    for row in results:
        print(row)

def query_users():
    global conn, cursor
    print("Search by:\n1. Username\n2. Phone\n3. All")
    choice = input("Enter choice (1/2/3): ")
    pagination = False
    batch_size = 10
    offset = 0

    if choice == "1":
        username = input("Enter username to search: ")
        cursor.execute("SELECT * FROM phonebook WHERE username ILIKE %s;", (f"%{username}%",))
        results = cursor.fetchall()
        for row in results:
            print(row)
    elif choice == "2":
        phone = input("Enter phone to search: ")
        cursor.execute("SELECT * FROM phonebook WHERE phone LIKE %s;", (f"%{phone}%",))
        results = cursor.fetchall()
        for row in results:
            print(row)
    elif choice == "3":
        batch_size = int(input("Enter the number to show: "))
        pagination = True
        # Start pagination loop and return after it's done
        while pagination:
            cursor.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s;", (batch_size, offset * batch_size))
            results = cursor.fetchall()
            if not results:
                print("No more results.")
                break
            for row in results:
                print(row)

            choice = input("Enter choice (u-up, d-down, q-exit): ")
            if choice == "u":
                if offset >= 1:
                    offset -= 1
                else:
                    print("Can't go higher.")
            elif choice == "d":
                offset += 1
            elif choice == "q":
                return
            else:
                print("Wrong input")
        
        return  # <-- Add this to avoid running code below
    else:
        print("Invalid choice")

def del_user():
    global conn, cursor
    user = input("Enter a username or a phone to delete: ")
    cursor.execute("SELECT * FROM phonebook WHERE username = %s OR phone = %s", (user, user))
    result = cursor.fetchall()
    if result:
        cursor.execute("DELETE FROM phonebook WHERE username = %s OR phone = %s;", (user, user))
        conn.commit()
    else:
        print("No such a user")

#insert_from_list() #used once to fill the table with dummy data
while True:
    print("\nPhoneBook Menu:")
    print("1. Add a user")
    print("2. Query users")
    print("3. Delete a user")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice == "1":
        console_input()  # Add a user
    elif choice == "2":
        query_users()  # Query users
    elif choice == "3":
        del_user()  # Delete a user
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice, please try again.")

def create_table():
    cursor.execute("""
    CREATE TABLE phonebook (
        username TEXT,
        phone TEXT,
        birth_date DATE,
        id SERIAL PRIMARY KEY
    );
    """)
    conn.commit()
    #only used once for creating a table

cursor.close()
conn.close()