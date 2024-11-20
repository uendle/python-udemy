class Pessoa:
    ano = 2023 # atributo da classe

    def __init__(self, nome, idade) -> None:
        self.nome= nome#atributos do objeto
        self.idade= idade

    @classmethod#torna o metodo um metodo de class
    def metodo_de_classe(cls):#cls significa que esse metodo recebe a classe Pessoa como argumento que automaticamente sera tratada pelos metodos do decorador
        #não da pra usara self pois esse tem acesso a class nao ao objeto 
        #esse metodo pode ser usado para automatizar a criaçao de instancias desse aclasse
        print('ola')

    @classmethod
    def criar_com_18(cls, nome):
        print('um jovem')
        return cls(nome, 18)

    @classmethod#
    def criar_com_30(cls, nome):
        print('um senhor')
        return cls(nome, idade= 30)

jovem = Pessoa.criar_com_18('uendle')
print(jovem.nome)

senhora = Pessoa.criar_com_30('lilian')
print(senhora.idade)