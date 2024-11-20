class Pessoa:
    cpf = 'cpf da classe pessoa'

    def __init__(self, nome, sobrenome):
        self.nome= nome
        self.sobrenome= sobrenome

    def falar(self):
        print('estou na superclasse!!')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar(self):
        print('estou na sub class!!')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf= 'cpf do aluno aluno'

c1= Cliente('uendle','souza')
c1.falar()
print(c1.cpf,end='\n\n')

a1= Aluno('jose', 'arruda')
a1.falar()
print(a1.cpf)