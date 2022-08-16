from flask import Flask, jsonify
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/categories')
def query_categories():
    result = db.querydata("select * from categories")
    return jsonify(result)

@app.route('/categories/<id>')
def query_categories_by_id(id):
    result = db.querydata("select * from categories where category_id=" + id)
    return jsonify(result)

@app.route('/products')
def query_products():
    result = db.querydata("select * from products")
    return jsonify(result)

@app.route('/products/<id>')
def query_products_by_id(id):
    result = db.querydata("select * from products where product_id=" + id)
    return jsonify(result)

app.run(host='0.0.0.0', port=8080)