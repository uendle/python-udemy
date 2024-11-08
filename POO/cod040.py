from datetime import date

class Pessoa:
    hoje = date.today()#variavel de escopo acessivel atraves do molde e compartilhada entre todas as instancias da classse
    # hoje = 2024

    def __init__(self, nome, idade) -> None:#retorna None
        self.nome = nome#variaveis de instancia , sao atributos dos objetos acessiveis atraves do self
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.hoje.year - self.idade
        # return f'{self.nome} - {Pessoa.hoje - self.idade}'


uendle = Pessoa('uendle', 36)
print(uendle.idade)
print(uendle.get_ano_nascimento())
# Pessoa.hoje= 2000
print(uendle.get_ano_nascimento())

lilian = Pessoa('lilian', 40)
print(lilian.idade)
print(lilian.get_ano_nascimento())

print(uendle.__dict__)#dicionario como todos os atributos da instancia
print(vars(uendle))#retorna um dicionario como todos os atributos da instancia
uendle.__dict__['sexo']= 'meu ovo'# adiciona novos conjunto chave valor
print(vars(uendle))#retorna um dicionario como todos os atributos da instancia
del uendle.__dict__['sexo']#remove um item do dicionario da instancia
print(vars(uendle))#retorna um dicionario como todos os atributos da instancia
dados = uendle.__dict__#coloca os atributos do objeto na variavel
nova_pessoa= Pessoa(**dados)#descompacta e passa para nova pessoa os atributos 
print(nova_pessoa.__dict__)

