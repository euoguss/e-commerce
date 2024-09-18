from flask import Flask, render_template, url_for
from routes.client import client_route
from routes.home import home_route
from routes.product import product_route
from database.database import BancoDeDados

app = Flask(__name__)
db = BancoDeDados()
db.connect()

app.register_blueprint(product_route)
app.register_blueprint(home_route)
app.register_blueprint(client_route, url_prefix='/client')

app.run(debug=True)
db.disconnect()