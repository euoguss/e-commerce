from flask import Flask, render_template, Blueprint

product_route = Blueprint("product", __name__)

@product_route.route("/add")
def add_prod():
    # adicionar produtos no site - post
    return render_template('form_prod.html')

@product_route.route("/gab")
def gab_card():
    # adicionar produtos no site - post
    return render_template('gabinete.html')

@product_route.route("/sata")
def ssd_sata():
    # adicionar produtos no site - post
    return render_template('ssd_sata.html')

@product_route.route("/watercooler")
def water_cooler():
    # adicionar produtos no site - post
    return render_template('watercooler.html')

@product_route.route("/fonte_for")
def fonte_for():
    # adicionar produtos no site - post
    return render_template('fonte.html')

