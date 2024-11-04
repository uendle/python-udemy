def soma(*args):
    valor = 0
    for i in args:
        valor += i
    return valor

def multiplicar(*args):
    valor = 1
    for i in args:
        valor *= i
    return valor

def executa(funcao):
    def chamar_funcao(*args):
               return funcao(*args)
    return chamar_funcao

s= executa(soma)
m= executa(multiplicar)

print(s(1,2,3,))
print(m(10,2,3,))