from database.database import BancoDeDados

db = BancoDeDados()
db.connect()

val = ('dias.gustavof@gmail.com', 'Gusta20210')
log = db.singin(val)
db.verify()
db.returnProd(6)
db.addCart()
db.returnProd(9)
db.addCart()


db.disconnect()