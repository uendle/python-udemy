"""descrição do programa

aqui e uma descrição do que o programa faz
essa parte deve ser bem explicada e revisada 
pois e a parte mais detalhada do projeto"""

from typing import Any


class Multiplicar:
    def __init__(self, multiplicador) -> None:
        self._multiplicador= multiplicador

    def __call__(self, funcao) -> Any:
        def metodo_funcao(*args, **kwargs):
            resultado= funcao(*args, **kwargs)
            return resultado * self._multiplicador
        
        return metodo_funcao

@Multiplicar(2)
def soma(x, y):
    return x + y

print(soma(2, 3))