import sqlite3
import getpass
import secrets
import string
from cryptography.fernet import Fernet

encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

cursor.execute('''
           CREATE TABLE IF NOT EXISTS passwords
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
           website TEXT NOT NULL,
           username TEXT NOT NULL,
           password TEXT NOT NULL
           )
           ''')

conn.commit()

cursor.execute('''
           CREATE TABLE IF NOT EXISTS users
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
           username TEXT NOT NULL,
           password TEXT NOT NULL
           )
           ''')

conn.commit()


def register_user():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    encrypted_password = cipher_suite.encrypt(password.encode()).decode()
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, encrypted_password),
    )
    conn.commit()
    print("User registration successful!")


def login():
    global username
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    if user:
        stored_password = user[2]
        decrypted_password = cipher_suite.decrypt(stored_password.encode()).decode()
        if password == decrypted_password:
            print("Login successful!")
            return True
    print("Login failed. Please try again.")
    return False


while True:
    print("\nPassword Manager:")
    print("\t1. Register")
    print("\t2. Change password")
    print("\t3. Add password")
    print("\t4. View passwords")
    print("\t5. Delete password")
    print("\t6. Exit")

    choice = input("Select an option: ")
    if choice == "1":
        register_user()
    elif choice == "2":
        change_password()
    elif choice == "3":
        add_password()
    elif choice == "4":
        view_passwords()
    elif choice == "5":
        delete_password()
    elif choice == "6":
        break
    else:
        print("Invalid choice! Please select again.")

conn.close()
