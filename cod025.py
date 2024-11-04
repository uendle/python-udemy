variavel_global=100

def soma (variavel_nonlocal, variavel_global, *args):
    variavel_global= 10
    variavel_nonlocal= 10
    return sum(*args)+ variavel_nonlocal * variavel_global


def operacao(funcao):
    variavel_nonlocal=10
    def executar(*args):
        nonlocal variavel_nonlocal
        global variavel_global
        variavel_global= 10
        return funcao(variavel_nonlocal,variavel_global, args)
    return executar

somando= operacao(soma)
print(somando(1,2,3,4,5))

somando2= operacao(soma)
print(somando(1,2,3,4,5,6))