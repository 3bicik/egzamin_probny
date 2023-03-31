#!./venv/bin/python3.10

from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase

USER = "postgres"
HOST = "localhost"
PASSWORD = "postgres"
DATABASE = "exam2"

CREATE_DB = f"CREATE DATABASE {DATABASE};"

try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    print("Connection successful.")
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DB)
        print("Database created")
    except DuplicateDatabase as e:
        print("Database exists: ", e)
    cnx.close()
except OperationalError as e:
    print("Connection error.")