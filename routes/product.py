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

@product_route.route("/ram")
def memory_ram():
    # adicionar produtos no site - post
    return render_template('ram.html')

@product_route.route("/mother_board")
def motherboard():
    # adicionar produtos no site - post
    return render_template('placa_mae.html')

@product_route.route("/rtx")
def graphicboard():
    # adicionar produtos no site - post
    return render_template('placa_video.html')

@product_route.route("/corsair")
def fonte_cor():
    # adicionar produtos no site - post
    return render_template('fonte_cor.html')

@product_route.route("/nvme")
def ssd_nvme():
    # adicionar produtos no site - post
    return render_template('ssd_nvme.html')

@product_route.route("/amd")
def proc_amd():
    # adicionar produtos no site - post
    return render_template('ryzen.html')


