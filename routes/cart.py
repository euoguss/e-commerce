from flask import Flask, Blueprint, render_template, request
from database.database import BancoDeDados

db = BancoDeDados()
cart_route = Blueprint("cart", __name__)

@cart_route.route("/cart", methods=['GET', 'POST'])
def cart():
    
    return render_template("cart.html")