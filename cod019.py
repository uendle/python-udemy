lista= [valor * 2 for valor in range(1,11) if valor % 2 == 0]
print(lista)

lista_produtos= [
    {'nome':'p1','preco':20},
    {'nome':'p2','preco':10},
    {'nome':'p3','preco':30},
]

novos_produtos = [
    {**produtos ,'preco':produtos['preco'] * 1.05} 
    if produtos['preco'] > 20 else {**produtos}
    for produtos in lista_produtos
]

print(*novos_produtos , sep='\n')