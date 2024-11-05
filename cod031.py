from itertools import count ,combinations, permutations,product

print(hasattr(count(),'__iter__'), ' e um iterator')
print(hasattr(count(),'__next__'),'e um iteravel')
print(hasattr(range(10),'__iter__'),' e um iterator')
print(hasattr(range(10),'__next__'),'e um iteravel')

for i in count():
    if i > 5:
        break

    print('loop da morte ',i)


lista=['a','e','i','o','u']

def imprimir(interator):
    print(*list(interator),sep='\n')

print('----------------------')
imprimir(combinations(lista,2))

print('----------------------')
imprimir(permutations(lista,2))

lista_de_produtos=[
    ['camisa','bermuda','cueca'],
    ['p','m','g'],
    ['verde','amarela','vermelha'],
]
imprimir(product(*lista_de_produtos))
