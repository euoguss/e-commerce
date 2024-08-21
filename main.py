from flask import Flask, render_template, url_for
from routes.client import client_route
from routes.home import home_route
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(client_route, url_prefix='/client')

app.run(debug=True)