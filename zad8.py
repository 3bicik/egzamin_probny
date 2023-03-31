#!./venv/bin/python3.10

from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

USER = "postgres"
HOST = "localhost"
PASSWORD = "postgres"
DATABASE = "exam2"

CREATE_USERS_TABLE = """CREATE TABLE users(
	id serial PRIMARY KEY,
	name varchar(60) NOT NULL,
	email varchar(60) NOT NULL UNIQUE,
	password varchar(60) NOT NULL
);
"""

CREATE_MESSAGES_TABLE = """CREATE TABLE messages(
	id serial PRIMARY KEY,
	user_id int NOT NULL,
	message text NOT NULL,
	FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);
"""

CREATE_ITEMS_TABLE = """CREATE TABLE Items(
	id serial PRIMARY KEY,
	name varchar(40) NOT NULL,
	description text NOT NULL,
	price decimal(7, 2) NOT NULL
);
"""

CREATE_ORDERS_TABLE = """
CREATE TABLE Orders(
	id serial PRIMARY KEY,
	description text NOT NULL
);
"""

CREATE_ITEMS_ORDERS_TABLE = """
CREATE TABLE ItemsOrders(
	id serial PRIMARY KEY,
	item_id int,
	order_id int,
	FOREIGN KEY(item_id) REFERENCES items(id) ON DELETE CASCADE,
	FOREIGN KEY(order_id) REFERENCES orders(id) ON DELETE CASCADE
);
"""

try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_USERS_TABLE)
        print("Table Users created")
    except DuplicateTable as e:
        print("Table exists: ", e)

    try:
        cursor.execute(CREATE_MESSAGES_TABLE)
        print("Table Messages created")
    except DuplicateTable as e:
        print("Table exists: ", e)

    try:
        cursor.execute(CREATE_ITEMS_TABLE)
        print("Table Messages created")
    except DuplicateTable as e:
        print("Table exists: ", e)

    try:
        cursor.execute(CREATE_ORDERS_TABLE)
        print("Table Messages created")
    except DuplicateTable as e:
        print("Table exists: ", e)

    try:
        cursor.execute(CREATE_ITEMS_ORDERS_TABLE)
        print("Table Messages created")
    except DuplicateTable as e:
        print("Table exists: ", e)
except OperationalError as e:
    print("Connection error.")