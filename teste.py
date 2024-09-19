from database.database import BancoDeDados

db = BancoDeDados()
db.connect()

val = ('silva.santos13652@gmail.com', '81273dkvjbjksdvknjbaf47897289')
resul = (db.singin(val))
db.verify()

db.disconnect()