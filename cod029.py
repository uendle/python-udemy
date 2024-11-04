from itertools import zip_longest

cidade=['salvador','ubatuba','belo horizonte']
sigla= ['ba','sp','mg','rj']

def verifica_maior(cidade, sigla):
    maior = cidade if len(cidade) > len(sigla) else sigla
    menor = cidade if len(cidade) < len(sigla) else sigla
    print('verifica_maior')

    def decorador(func):
        print('decorador')

        def ziper(): 
            print('ziper') 
            return func(maior,menor)
        return ziper
    return decorador

@verifica_maior(cidade ,sigla)
def juntar(max,min):
    l=[]
    con= 0
    for i in min:
        l.append((min[con],max[con]))
        con+= 1
    return(l)

print(juntar())

print('----------zip--------------')

print(list(zip(cidade,sigla)))

print('----------zip_longest--------------')
print(list(zip_longest(cidade,sigla)))

print('----------zip_longest--------------')
print(list(zip_longest(cidade,sigla,fillvalue='valor padrao')))