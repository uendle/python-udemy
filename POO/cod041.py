import json

class Pessoa:
    def __init__(self, nome ,sexo ) -> None:
        self.nome = nome
        self.sexo = sexo
    

uendle = Pessoa('uendle', 'masculino')
lilian= Pessoa('lilian','feminino')
bernardo= Pessoa('bernardo','masculino')

lista=[uendle.__dict__, vars(lilian), bernardo.__dict__]


with open('arquivo.json', 'w',encoding='utf-8') as bd:
    json.dump(lista, bd , ensure_ascii=False ,indent= 2)

        