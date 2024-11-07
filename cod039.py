import json

with open('arquivo.json','r',encoding='utf8') as arquivo:
    pessoa= json.load(arquivo)

    print(pessoa['nome'])