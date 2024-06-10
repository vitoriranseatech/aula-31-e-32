class cadastro:
    nome = Ana

    def __init__(self):
        print("construtor")

    def validarnome(self, nome):
        if len(nome) == 0:
            print("o valor nome não pode ser vazio")
        else:
            self.nome = nome
            print("valor cadastro com sucesso")

cadastro1 = Cadastro()
cadastro1.validarNome("Ana")