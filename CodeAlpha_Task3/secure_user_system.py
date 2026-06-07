import sqlite3
import bcrypt

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

while True:

    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":

        username = input("Username: ")
        password = input("Password: ")

        hashed = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, hashed)
        )

        conn.commit()

        print("Registration Successful")

    elif choice == "2":

        username = input("Username: ")

        password = input("Password: ")

        cursor.execute(
            "SELECT password FROM users WHERE username=?",
            (username,)
        )

        result = cursor.fetchone()

        if result and bcrypt.checkpw(
            password.encode(),
            result[0]
        ):
            print("Login Successful")

        else:
            print("Invalid Credentials")

    elif choice == "3":
        break