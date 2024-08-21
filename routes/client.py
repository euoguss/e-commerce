from flask import Flask, Blueprint, render_template

client_route = Blueprint("client", __name__)

@client_route.route("/acount")
def acount():
    return render_template("acount.html")