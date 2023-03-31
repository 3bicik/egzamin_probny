from flask import Flask, request

app = Flask(__name__)

def factorial(num):
    result = 1
    for i in range(2, num+1):
        result *= i
    return result

@app.route('/', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return """
            <form action='/', method='POST'>
                <label for="number">
                    Enter a natural number
                </label><br>
                <input type="number" name="number" min="0" oninput="validity.valid||(value='');"><br>
                <label>
                    <button type="submit">
                        Submit
                    </button>
                </label><br>
            </form>

        """
    elif request.method == 'POST':
        number = int(request.form["number"])
        print(number)
        return f"""
            <table>
              <tr>
                <th> 2^{number}</th>
                <td> {2 ** number} </td>
              </tr>
              <tr>
                <th>{number}^{number} </th>
                <td> {number ** number} </td>
              </tr>
              <tr>
                <th>factorial({number}) </th>
                <td> {factorial(number)} </td>
              </tr>
            </table>
        """


if __name__ == '__main__':
    app.run()