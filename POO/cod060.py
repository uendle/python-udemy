from typing import Any


class CallMe:
    def __init__(self, numero) -> None:
        self.phone= numero

    def __call__(self, nome) -> Any:#sempre sera executado 
        print(nome,' esta te ligando ', self.phone)
        return True
    
liga= CallMe('123456789')
print(liga('uendle'))
