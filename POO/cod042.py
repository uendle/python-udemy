import json
from cod041 import Pessoa
dados= {}
lista_pessoa=[]

with open('arquivo.json', 'r', encoding='utf8') as bd:
    dados = json.load(bd)

for item in dados:
    lista_pessoa.append(Pessoa(**item))

for item in lista_pessoa:
    print(item.__dict__)