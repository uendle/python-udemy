def decorador_classe(cls):
    def metodo_do_decorador(self):
        class_nome= self.__class__.__name__
        class_dict= self.__dict__
        class_repr= f'{class_nome} ({class_dict})'
        return class_repr
    cls.__repr__ = metodo_do_decorador
    return cls

def decorador_metodo(metodo):
    def metodo_do_decorador(self, *args, **kwargs):
        resultado = metodo(self,*args, **kwargs)

        if 'TERRA' in resultado:
            return 'Voce esta em casa'
        
        return resultado
    return metodo_do_decorador




@decorador_classe
class Time:
    def __init__(self, nome) -> None:
        self.nome= nome
@decorador_classe
class Planeta:
    def __init__(self, nome) -> None:
        self.nome= nome
    @decorador_metodo
    def falar(self):
        return f'o planeta é {self.nome}'

t1= Time('VASCO')
t2= Time('FLAMENGO')

P1= Planeta('TERRA')
P2= Planeta('JUPITER')

print(t1)
print(t2)

print(P1)
print(P2)

print(P1.falar())
print(P2.falar())