from flask import Flask, render_template, Blueprint, request
from database.database import BancoDeDados
db = BancoDeDados()
product_route = Blueprint("product", __name__)

@product_route.route("/add", methods=['GET', 'POST'])
def add_prod():
    if request.method == "POST":
        Cod = request.form['Cod']
        Nome = request.form['Nome']
        Desc = request.form['Desc']
        Preco = request.form['Preco']
        Categ = request.form['Categ']
        Quant = request.form['Quant']
        values = (int(Cod),Nome,Desc,float(Preco),Categ,int(Quant))
        db.addProd(values)
        return render_template("form_add_prod.html")
    return render_template('form_add_prod.html')

@product_route.route('/armazenamento')
def arm():
    return render_template('armazenamento.html')

@product_route.route('/alimentacao')
def alim():
    return render_template('alimentacao.html')

@product_route.route("/gab", methods=['GET', 'POST'])
def gab_card():
    if request.method == "POST":
        values = (1)
        prod = db.returnProd(values)
        if prod == None:
            return render_template("login.html")
        db.addCart(prod)
        return render_template("index.html")
    return render_template('gabinete.html')

@product_route.route("/sata")
def ssd_sata():
    if request.method == "POST":
        values = (2)
        prod = db.returnProd(values)
        if prod == None:
            return render_template("login.html")
        db.addCart(prod)
        return render_template("index.html")
    return render_template('ssd_sata.html')

@product_route.route("/watercooler")
def water_cooler():
    if request.method == "POST":
        values = (3)
        prod = db.returnProd(values)
        if prod == None:
            return render_template("login.html")
        db.addCart(prod)
        return render_template("index.html")
    return render_template('watercooler.html')

@product_route.route("/fonte_for")
def fonte_for():
    if request.method == "POST":
        values = (4)
        prod = db.returnProd(values)
        if prod == None:
            return render_template("login.html")
        db.addCart(prod)
        return render_template("index.html")
    return render_template('fonte.html')

@product_route.route("/ram")
def memory_ram():
    if request.method == "POST":
        values = (5)
        prod = db.returnProd(values)
        if prod == None:
            return render_template("login.html")
        db.addCart(prod)
        return render_template("index.html")
    return render_template('ram.html')

@product_route.route("/mother_board")
def motherboard():
    if request.method == "POST":
        values = (6)
        prod = db.returnProd(values)
        if prod == None:
            return render_template("login.html")
        db.addCart(prod)
        return render_template("index.html")
    return render_template('placa_mae.html')

@product_route.route("/rtx")
def graphicboard():
    if request.method == "POST":
        values = (7)
        prod = db.returnProd(values)
        if prod == None:
            return render_template("login.html")
        db.addCart(prod)
        return render_template("index.html")
    return render_template('placa_video.html')

@product_route.route("/corsair")
def fonte_cor():
    if request.method == "POST":
        values = (8)
        prod = db.returnProd(values)
        if prod == None:
            return render_template("login.html")
        db.addCart(prod)
        return render_template("index.html")
    return render_template('fonte_cor.html')

@product_route.route("/nvme")
def ssd_nvme():
    if request.method == "POST":
        values = (9)
        prod = db.returnProd(values)
        if prod == None:
            return render_template("login.html")
        db.addCart(prod)
        return render_template("index.html")
    return render_template('ssd_nvme.html')

@product_route.route("/amd")
def proc_amd():
    if request.method == "POST":
        values = (10)
        prod = db.returnProd(values)
        if prod == None:
            return render_template("login.html")
        db.addCart(prod)
        return render_template("index.html")
    return render_template('ryzen.html')


