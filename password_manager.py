import sqlite3
import getpass
import secrets
import string
from cryptography.fernet import Fernet

encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

conn = sqlite3.connect("passwords.db")
c = conn.cursor()
