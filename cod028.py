def parametros_decorador(nome):
    def decorador(func):
        print('decorador:',nome)

        def sua_nova_funcao(*args,**kwarg):
            res= func(*args,**kwarg)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='quarto')
@parametros_decorador(nome='terceiro')
@parametros_decorador(nome='segundo')
@parametros_decorador(nome='primeiro')
def soma(x,y):
    return x + y

print(soma(2,3))