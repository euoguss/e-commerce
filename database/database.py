import mysql.connector
class BancoDeDados:
    
    def __init__(self, conexao = mysql.connector.connect(user='root', password='', host='localhost', database='mydb'), login = [], produtos = [], carrinho = {}):
        self.conexao = conexao
        self.login = login
        self.produtos = produtos
        self.carrinho = carrinho

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
        
        except:
            print("Erro ao inserir o usuario")
            return None

    def singin(self, values):
        cursor = self.conexao.cursor()
        try:
            sql = "SELECT * FROM clientes WHERE Email = %s AND Senha = %s"
            cursor.execute(sql, values)
            for row in cursor:
                for d in row:
                    self.login.append(d)
            print(f'Os dados são {self.login}')
            cursor.close()
            return self.login
        except:
            print("Erro ao buscar o usuario")
            return None

    

    def verify(self):
        try:
            if self.login != []:
                values = self.login
                    
                self.login = {'Cpf' : values[0], 'Nome' : values[1],'Email' : values[2],'Senha' : values[3], 'Tel' : values[4], 'Ender' : values[5], 'Nasc' : values[6]}
                
                print(f'Login verificado com sucesso {self.login}')
                return self.login
            return None
        except:
            print('Erro ao verificar o login')
            return None

    def disconnect(self):
        self.conexao.close()
        print('Desconectado do banco')

    def returnProd(self, values):
        cursor = self.conexao.cursor()
        try:
            print(values)
            sql = "SELECT * FROM produtos WHERE CodProduto = %s"
            cursor.execute(sql, (values,))
            for row in cursor:
                for d in row:
                    self.produtos.append(d)
            print(f'Os dados são {self.produtos}')
            cursor.close()
            return self.produtos
        except:
            print("Erro ao buscar o produto")
            return None
    
    def addCart(self):
        cursor = self.conexao.cursor()
        if self.produtos != None:
            try:
                sql = "INSERT INTO carrinho(IdCarrinho, CodProduto, Quantidade, Preco) VALUES (%s, %s, %s, %s)"
                values = (len(self.carrinho) + 1, self.produtos[0], self.produtos[5], self.produtos[3])             
                print(values)
                cursor.execute(sql, values)
                self.conexao.commit()
                print(f'{cursor.rowcount} registro inserido.')
                self.carrinho[self.produtos[1]] = values
                print("Produto inserido com sucesso")
                print(self.carrinho)
                cursor.close()
            except:
                print("Erro ao inserir o produto")
                return None

    def addProd(self, values):
        cursor = self.conexao.cursor()
        try:
            sql = "INSERT INTO produtos(CodProduto, Nome, Descricao, Preco, Categoria, Quantidade) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, values)
            self.conexao.commit()
            print(f'{cursor.rowcount} registro inserido.')
            cursor.close()
            return "Produto inserido com sucesso"
        except:
            print("Erro ao inserir o produto")
            return None