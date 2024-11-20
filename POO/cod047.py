class Carrinho:
    def __init__(self) -> None:
        self._produtos= []

    def listar_produtos(self):
        for i in self._produtos:
            print(i.nome,i.preco, end='\n')
    
    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)#inseri os itens na lista
      # self._produtos += produtos

    def total(self):
        return sum([p.preco for p in self._produtos])
    

class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco


car = Carrinho()
p1, p2 = Produto('ovo',1.5),Produto('carne', 2.3)

car.inserir_produtos(p1,p2)

car.listar_produtos()
print(car.total())