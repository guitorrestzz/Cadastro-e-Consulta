from controllers.sql import Banco

class Cliente:
    def __init__(self, nome = None, email = None, telefone = None):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.banco = Banco()

    def inserir_dados(self):
        try:
            dados = {
                'nome' : self.nome,
                'email': self.email,
                'telefone' : self.telefone
            }
            self.banco.inserir('tb_clientes', dados)
            print("Cliente.py | Inserir Dados | Cadastrado com sucesso")
        except:
            print("Cliente.py | Inserir Dados | Erro ao cadastrar")
    
    def consultar_dados(self):
        try:
            dados = self.banco.consultar('tb_clientes')
            print("Cliente.py | Consultar Dados | Consultado com sucesso")
            return dados
        except:
            print("Cliente.py | Consultar Dados | Erro ao consultar")
