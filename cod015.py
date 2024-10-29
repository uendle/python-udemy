dicionerio = {'chave1':1,'chave1':2,'chave3':3}
print(dicionerio.get('chave4','Não existe esta chave'))

if dicionerio.get('chave1') is None:
    print('chave inexistente')
else:
    print(dicionerio['chave1'])