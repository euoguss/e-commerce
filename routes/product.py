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


