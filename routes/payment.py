from flask import Flask, render_template, Blueprint

pay_route = Blueprint("payment", __name__)

@pay_route.route("/add")
def add_met_pay():
    return render_template('form_add_payment.html')