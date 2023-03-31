import bcrypt
import random
import string
import mysql.connector
from datetime import datetime


def generate_email(length=10):
    username = ''.join(random.choices(string.ascii_lowercase, k=length))
    domain = ''.join(random.choices(string.ascii_lowercase, k=length))
    return f"{username}@{domain}.com"


def generate_phone():
    return ''.join(random.choices(string.digits, k=11))


def generate_created_at():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="SecurePasswordEasyToGuess",
    database="research_10_db"
)

with open("users.txt", "r") as user_file, open("passwords.txt", "r") as password_file:
    usernames = [line.strip() for line in user_file]
    passwords = [line.strip() for line in password_file]

hashed_passwords = [bcrypt.hashpw(
    password.encode(), bcrypt.gensalt()) for password in passwords]

if len(usernames) != len(hashed_passwords) or len(usernames) != len(passwords):
    print("Error: Lengths of input lists do not match.")
else:
    cursor = db.cursor()
    for i in range(len(usernames)):
        email = generate_email()
        phone = generate_phone()
        created_at = generate_created_at()
        sql = "INSERT INTO users (username, email, password_hash, phone, created_at) VALUES (%s, %s, %s, %s, %s)"
        val = (usernames[i], email, hashed_passwords[i], phone, created_at)
        cursor.execute(sql, val)

    db.commit()

    cursor.close()
    db.close()
