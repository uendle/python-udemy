class Ponto:
    def __init__(self, x, y) -> None:
        self.x= x
        self.y= y

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    #para desenvolvedores ,so sera executado na ausencia do __str__
    def __repr__(self) -> str:
        class_name = type(self).__name__
       # class_name = self.__class__.__name__
        return f'{class_name}  (x={self.x!r}, y={self.y!r})'
    
    def __add__(self, other):
        novo_x= self.x + other.x
        novo_y= self.y + other.y
        return Ponto(novo_x, novo_y)
    
    def __gt__(self, other):
        soma_self= self.x + self.y
        soma_other= other.x + other.y
        return soma_self > soma_other

    
if __name__ == '__main__':
    p1= Ponto(1,2)
    p2= Ponto(123,234)
    p3= p1 + p2

    print(p1)
    print(repr(p2))#metod retorna a presentaçao do __repr__
    print(f'{p3!r})')#retorna a presentaçao do __repr__v
    print(p1 > p2)
    print(p2 > p1)