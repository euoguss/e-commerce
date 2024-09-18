from flask import Flask, Blueprint, render_template, request
from database.database import BancoDeDados

db = BancoDeDados()
client_route = Blueprint("client", __name__)

# @client_route.route("/add")
# def add_client():
#     return render_template("form_add_user.html")

@client_route.route("/add", methods=['GET', 'POST'])
def singup():
    if request.method == "POST":
        Nome = request.form['Nome']
        Email = request.form['Email']
        Senha = request.form['Senha']
        Cpf = request.form['Cpf']
        Nasc = f"{request.form['NascA']}-{request.form['NascM']}-{request.form['NascD']}"
        Ender = request.form['Ender']
        Tel = request.form['Tel']
        values = (Cpf,Nome,Email,Senha,Tel,Ender,Nasc)
        db.singup(values)
        return render_template("login.html")
        # print(values)

        ...
    # data = request.json
    # print(data)
    # values = (data)
    # 
    return render_template("form_add_user.html")
    ...

@client_route.route("/login", methods=['GET', 'POST'])
def singin():
        if request.method == "POST":
            Email = request.form['Email']
            Senha = request.form['Senha']
            values = (Email,Senha)
            db.singin(values)
            return render_template("index.html")
        return render_template("login.html")

@client_route.route("/acount")
def acount():
    return render_template("acount.html", dados = db.verify())

@client_route.route("/cart")
def cart():
    
    return render_template("cart.html")