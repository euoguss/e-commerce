from database.database import BancoDeDados

db = BancoDeDados()
db.connect()

val = ('dias.gustavof@gmail.com', 'Gusta20210')
log = db.singin(val)
db.verify()
cod = '1'
db.returnProd(cod)
db.addCart()

db.disconnect()