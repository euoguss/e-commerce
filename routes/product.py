from flask import Flask, render_template, Blueprint

product_route = Blueprint("product", __name__)

@product_route.route("/add")
def add_prod():
    # adicionar produtos no site - post
    return render_template('form_prod.html')from flask import Flask, render_template, Blueprint

product_route = Blueprint("product", __name__)

@product_route.route("/add")
def add_prod():
    # adicionar produtos no site - post
    return render_template('form_prod.html')

@product_route.route("/gab")
def gab_card():
    # adicionar produtos no site - post
    return render_template('gabinete.html')