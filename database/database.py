import mysql.connector
class BancoDeDados:
    
    def __init__(self, conexao = mysql.connector.connect(user='root', password='', host='localhost', database='mydb'), login = []):
        self.conexao = conexao
        self.login = login
        

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
            sql = "SELECT * FROM clientes WHERE Email = %s AND Senha = %s"
            cursor.execute(sql, values)
            self.login = []
            for row in cursor:
                for d in row:
                    self.login.append(d)
            print(f'Os dados são {self.login}')
            cursor.close()
            return self.login
        except:
            print("Erro ao buscar o usuario")

    

    def verify(self):
        try:
            if self.login != []:
                values = self.login
                # for v in values:
                #     print(v)
                    # self.login.get(value).append(values[value])
                    
                self.login = {'Cpf' : values[0], 'Nome' : values[1],'Email' : values[2],'Senha' : values[3], 'Tel' : values[4], 'Ender' : values[5], 'Nasc' : values[6]}
                
                print(f'Login verificado com sucesso {self.login}')
                return self.login
            return None
        except:
            print('Erro ao verificar o login')
            return None
    
    def addCart(self):
        
        self.conexao.close()

    def disconnect(self):
        self.conexao.close()
        print('Desconectado do banco')
