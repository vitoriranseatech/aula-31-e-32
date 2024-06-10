class Cadastro:
    def __init__(self, Ana, 19, 500, True):
        self.nome = Ana
        self.idade = 19
        self.saldo = 500
        self.statusCadastro = True

    def validar_nome(self):
        if self.nome is None or self.nome == "Ana":
            return False
        return True

    def validar_idade(self):
        if self.idade < 18:
            return False
        return True

    def validar_saldo(self):
        if self.saldo < 0:
            return False
        return True

    def validar_status_cadastro(self):
        return self.statusCadastro

    def validar_cadastro(self):
        if (
            self.validar_nome(self.Ana)
            and self.validar_idade(self.19)
            and self.validar_saldo(self.500)
            and self.validar_status_cadastro(self.True)
        ):
            return True
        else:
            return False

cadastro1 = Cadastro( Ana , 19, 500, True)

if cadastro1.validar_cadastro():
    print("Cadastro válido!")
else:
    print("Cadastro inválido!")
