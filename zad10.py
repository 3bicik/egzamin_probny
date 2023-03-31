from flask import Flask, request
from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateTable

app = Flask(__name__)

USER = "postgres"
HOST = "localhost"
PASSWORD = "postgres"
DATABASE = "exam2"

@app.route('/add_product', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return """
            <form action='/add_product', method='POST'>
                <label for="name">
                    Name
                </label><br>
                <input type="text" name="name"><br>
                <label for="number">
                    Description
                </label><br>
                <input type="text" name="description"><br>
                <label for="Price">
                    Price
                </label><br>
                <input type="number" name="price" min="0" step="0.01" oninput="validity.valid||(value='');"><br>
                <label>
                    <button type="submit">
                        Submit
                    </button>
                </label><br>
            </form>
        """
    elif request.method == 'POST':
        name = request.form["name"]
        description = request.form["description"]
        price = request.form["price"]
        sql = f"""
            INSERT INTO items(name, description, price) VALUES('{name}', '{description}', '{price}')
        """
        if name and description and price:
            try:
                cnx = connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
                cnx.autocommit = True
                cursor = cnx.cursor()
                try:
                    cursor.execute(sql)
                    if cursor.rowcount == 1:
                        result = "Product added!"
                    else:
                        result = "Failed adding product!"
                except DuplicateTable as e:
                    print("Table exists: ", e)
                cnx.close()
            except OperationalError as e:
                print("Connection error.")
        else:
            result = "Invalid data!"
        return result


if __name__ == '__main__':
    app.run()