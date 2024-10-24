lista= ['a','b','c','d']
lista_enumerada= enumerate(lista)

for i in lista_enumerada:
    print(i)
print('-----------------------')

for indice, item in enumerate(lista):
    print(indice , item)
print('-----------------------')

for indice, item in enumerate(lista, start=5):
    print(indice , item)