import psycopg2
import csv

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="kaz130212",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

def console_input():
    global conn, cursor
    username = str(input("Enter name: "))
    phone = int(input("Enter phone: "))
    birth_date = input("Enter birth date (YYYY-MM-DD): ")

    cursor.execute("""
        INSERT INTO phoneBook (username, phone, birth_date)
        VALUES (%s, %s, %s);
    """, (username, phone, birth_date))

    conn.commit()
    print("Data inserted from console")

def csv_input(filename):
    global conn, cursor
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO phoneBook (username, phone, birth_date)
                VALUES (%s, %s, %s);
            """, (row['username'], row['phone'], row['birth_date']))
    conn.commit()
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
        UPDATE phoneBook
        SET {field} = %s
        WHERE username = %s OR phone = %s;
    """, (new_value, identifier, identifier))

    conn.commit()
    print("Updated successfully")

def query_users():
    global conn, cursor
    print("Search by:\n1. Username\n2. Phone\n3. All")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "1":
        username = input("Enter username to search: ")
        cursor.execute("SELECT * FROM phoneBook WHERE username ILIKE %s;", (f"%{username}%",))
    elif choice == "2":
        phone = input("Enter phone to search: ")
        cursor.execute("SELECT * FROM phoneBook WHERE phone LIKE %s;", (f"%{phone}%",))
    elif choice == "3":
        cursor.execute("SELECT * FROM phoneBook;")
    else:
        print("Invalid choice")
        return

    results = cursor.fetchall()
    for row in results:
        print(row)

def del_user():
    global conn, cursor
    user = input("Enter a username or a phone to delete: ")
    cursor.execute("DELETE FROM phoneBook WHERE username = %s OR phone = %s;", (user, user))
    conn.commit()
    print(f"Deleted: {user}")

#main loop to use database
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

# cursor.execute("""
# CREATE TABLE postgres (
#     id SERIAL PRIMARY KEY,
#     username TEXT,
#     phone TEXT,
#     birth_date DATE 
# );
# """)
# conn.commit()
# #only used once for creating a table

cursor.close()
conn.close()