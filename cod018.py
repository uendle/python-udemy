def executa(funcao , *args):
    return funcao(*args)

def multiplicar(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


valor = multiplicar(5)
valor1 = multiplicar(10)

valor2 = executa(lambda m :lambda  n : n * m ,2)



print(valor(5))
print(valor1(10))
print(valor2(5))
#print(valor1(10))
