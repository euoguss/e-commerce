import mysql.connector
from controller.controller import login
log = login()
class bancoDeDados:
    
    def __init__(self, conexao = mysql.connector.connect(user='root', password='', host='localhost', database='mydb')):
        self.conexao = conexao
        

    def connect(self):
        if self.conexao.is_connected():
            print('Conectado ao banco')

    def singup(self, values):
        cursor = self.conexao.cursor()

        try:
            sql = "INSERT INTO clientes(CPF, Nome, Email, Senha, Telefone, Endereco, Nascimento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            
            cursor.execute(sql, values)
            self.conexao.commit()
            
            print(f'{cursor.rowcount} registro inserido.')
            cursor.close()
            return "Usuario inserido com sucesso"
            ...
        except:
            return "Erro ao inserir o usuario"
            ...
        ...

    def singin(self, values):
        cursor = self.conexao.cursor()
        try:
            sql = "SELECT * FROM clientes WHERE Email = %s AND Senha = %d"
            
            cursor.execute(sql, values)
            result = cursor.fetchall()
            log.verify(result)
            cursor.close()
            return f'{result}'
        except:
            return "Erro ao buscar o usuario"

    def disconnect(self):
        self.conexao.close()