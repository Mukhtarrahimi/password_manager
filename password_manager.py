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
