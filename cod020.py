
lista = [iten if iten != 6 else 'seis' for iten in range(0,10) if iten % 2 == 0 ]

lista2= [(x,y) if x != 1 else ('um',y)
          for x in range(1,6)
          for y in range(1,6)]

nome = 'uendle dos santos souza'
string= "".join([letra for letra in nome])

dic={
    "nome":'uendle',
    "idade":32,
    "altura":1.88,
}

dicionario ={
    chave:valor.upper()
    if isinstance(valor,str)else valor
    for chave , valor in dic.items()
    if chave != "idade"
}



print(lista)
print(lista2)
print(string)
print(dicionario)