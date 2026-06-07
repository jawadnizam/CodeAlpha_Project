import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
username TEXT,
password TEXT
)
""")

conn.commit()

print("===== USER MANAGEMENT SYSTEM =====")

while True:

    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        username = input("Username: ")
        password = input("Password: ")

        query = f"INSERT INTO users(username,password) VALUES('{username}','{password}')"

        cursor.execute(query)

        conn.commit()

        print("User Registered Successfully")

    elif choice == "2":

        username = input("Username: ")
        password = input("Password: ")

        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

        result = cursor.execute(query)

        user = result.fetchone()

        if user:
            print("Login Successful")
        else:
            print("Invalid Credentials")

    elif choice == "3":
        break
