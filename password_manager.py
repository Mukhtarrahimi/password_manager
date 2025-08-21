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