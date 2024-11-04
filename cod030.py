l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5,6,7]

menor_lista = l1 if l1 < l2 else l2


lista_dobrado = []
i=0
while i < len(menor_lista):
    lista_dobrado.append(l1[i] + l2[i])
    i+=1
print(lista_dobrado)



lista_dobrado = []
for i , _ in enumerate(menor_lista):
    lista_dobrado.append(l1[i] + l2[i])
print(lista_dobrado)




lista_dobrado = [l1[i] + l2[i]
                 for i in range(len(menor_lista))]
print(lista_dobrado)


lista_dobrado = [x + y for x,y in zip(l1,l2)]
print(lista_dobrado)