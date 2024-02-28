from flask import Flask, request, jsonify
import products_dao
from get_connection import get_sql_connection

connection = get_sql_connection()

app = Flask(__name__)

@app.route('/getProducts')
def hello():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":

    app.run(port=5000)