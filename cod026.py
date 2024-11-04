
def operacao(funcao):
    def executar(*args):
        return funcao(*args)

    return executar

@operacao #decoradores
def soma (*args):
    return sum(args)
@operacao
def multi (a,b):
    return a* b

print(soma(1,2))
print(multi(4,5))


