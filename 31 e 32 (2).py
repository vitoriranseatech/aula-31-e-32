class aluno:
    cadastroValido = True
    idade = 17

    def __init__(self):
        print("construindo objeto")

    def inserirIdade(self, idade):
        idadeCorreta = self.validar_idade(idade)
        if idadeCorreta == True:
           self.idade == idade
           print("idade cadastrada com sucesso", idade)
        else:
            print("idade invalida. a idade precisa ser maior que 0")

    def validar_idade(self, idade):
        if idade <=0:
            print("a idade não pode ser menor que 0")

    def imprimir_idade(self):
        print(self.idade)

aluno1 = Aluno() 
aluno1.inserirIdade(-10)
aluno1.imprimir_idade()