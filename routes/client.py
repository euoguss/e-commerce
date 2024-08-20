from flask import Flask, Blueprint

client_route = Blueprint("client", __name__)

# @client_route.route("/")