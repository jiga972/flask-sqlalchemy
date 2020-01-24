#import os
#import logging

#logging.warn(os.environ["DUMMY"])

from flask import Flask, render_template
from config import Config
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
app = Flask(__name__)
app.config.from_object(Config)


from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Product
from schemas import products_schema

admin = Admin(app, template_mode='bootstrap3')
admin.add_view(ModelView(Product, db.session))

@app.route('/')
def home():
    products = db.session.query(Product).all()


    return render_template('home.html', products=products)

@app.route('/<int:id>')
def product_html(id):
    product = db.session.query(Product).get(id)
    return render_template('product.html', product=product)

#@app.route('/products', methods=["GET"])
#def get_products():
#   products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
#   return products_schema.jsonify(products)

#@app.route('/products/<int:id>', methods=["GET"])
#def get_product(id):
#    product = db.session.query(Product).get(id) # SQLAlchemy request => 'SELECT * FROM products'
 #   return product_schema.jsonify(product)

#@app.route('/products', methods=["POST"])
#def post_product():
#    product = Product(name="Jimmy")
#    db.session.add(product)
#    db.session.commit() # SQLAlchemy request => 'SELECT * FROM products'
#    return product_schema.jsonify(product)

#@app.route('/products/<int:id>', methods=["DELETE"])
#def delete_product(id):
#    product = db.session.query(Product).get(id)
#    db.session.delete(product)
#    db.session.commit()
#    return product_schema.jsonify(product)


#@app.route('/hello')
#def hello():
#    return "Hello World!"
