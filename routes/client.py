from flask import Flask, Blueprint, render_template

client_route = Blueprint("client", __name__)

@client_route.route("/add")
def add_client():
    return render_template("form_add_user.html")

@client_route.route("/acount")
def acount():
    return render_template("acount.html")