import sqlite3
import getpass
import secrets
import string
from cryptography.fernet import Fernet

encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

conn = sqlite3.connect("passwords.db")
c = conn.cursor()

c.execute('''
           CREATE TABLE IF NOT EXISTS passwords
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
           website TEXT NOT NULL,
           username TEXT NOT NULL,
           password TEXT NOT NULL
           )
           ''')

conn.commit()

c.execute('''
           CREATE TABLE IF NOT EXISTS users
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
           username TEXT NOT NULL,
           password TEXT NOT NULL
           )
           ''')

conn.commit()

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
