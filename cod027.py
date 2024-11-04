# https://pythoniluminado.netlify.app/decoradores
def fabrica_decoradores(a=None,b=None,c=None):
    def fabrica_funcoes(func):
        def aninhada(*args, **kwargs):
            return func(*args, **kwargs)
            
        return aninhada
    return fabrica_funcoes


@fabrica_decoradores(1,2,3)
def soma(x, y):
    return x +y


print(soma(1,2))

multiplica= fabrica_decoradores(1,2,3)(lambda x,y: x*y)
print(multiplica(2,3))
