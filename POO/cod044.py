class Classe:
    @staticmethod#nao tem acesso a class nem ao objeto
    def praticamente_uma_funcao(*args, **kwargs):
        print(f'oi {args} {kwargs}')

def mesma_coisa(*args, **kwargs) :
    print(f'oi {args} {kwargs}')

obj= Classe()
obj.praticamente_uma_funcao([i for i in range(10)],'abc',nome=1)

mesma_coisa([i for i in range(10)],'abc',nome=1)