from database.database import BancoDeDados

db = BancoDeDados()
db.connect()

val = ('dias.gustavof@gmail.com', '8127347897289')
resul = (db.singin(val))
db.verify()

db.disconnect()