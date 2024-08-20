import mysql.connector

# Conectando ao banco de dados

base = mysql.connector.connect(
    user='root', password='',
    host='127.0.0.1',
    database='ecommerce'
)


try: 
    # Criando as tabelas

    TABLES = {}
    TABLES['']

except:
    ...

base.close()