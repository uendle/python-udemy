from copy import deepcopy
import pacote.produto#importa minha lista produtos

produtos_atualizados = deepcopy(pacote.produto.produtos)#cria uma copia sem referencia
 
produtos_atualizados = [
    {**dic,'valor':round(dic['valor'] * 1.1,2 )}
    for dic in pacote.produto.produtos
]
print(*produtos_atualizados, sep='\n')

print('--------------nome-decrecente--------------',end='\n\n')
produtos_ordenado_nome_reverse=sorted(produtos_atualizados,key=lambda x: x['nome'],reverse=True)
print(*produtos_ordenado_nome_reverse,sep='\n')


print('--------------valor---------------',end='\n\n')
#rodutos_ordenados_valor=deepcopy(produtos_ordenado_nome_reverse)
produtos_ordenados_valor=sorted(deepcopy(produtos_atualizados),key=lambda x : x['valor'])
print(*produtos_ordenados_valor,sep='\n')
