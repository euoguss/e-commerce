class login:
    def __init__(self,login = None):
        self.login = login
        pass

    def verify(self, values):
        login = {'Cpf' : values[0], 'Nome' : values[1],'Email' : values[2],'Senha' : values[3], 'Tel' : values[4], 'Ender' : values[5], 'Nasc' : values[6]}
        return login
        ...