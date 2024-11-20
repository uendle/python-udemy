class Caneta:
    def __init__(self, cor) -> None:
        self._cor = cor
    
    def get_cor(self):#encapsulamento do atributo evitando quebrar o programa
        print('metodo_get')

        return self._cor
    
    @property#tambem encapsula , e permite cahmar o objeto como se fosse o atributo do objeto
    def cor(self):
        print('property')
        return self._cor
    
    @cor.setter#encapsula e permite atribuir valor no metodo como se fosse um atributo
    def cor(self, cor):
        print('@nomedo do metodo . setter')
        self._cor = cor
    

obj=Caneta('azul')
print(obj.get_cor())#cama o metodo get
print(obj.cor)#chama o property , nao necessita do ()

obj.cor= 'vermelho'#atribui valor a instancia atraves do metodo decorad com setter
print(obj.cor)#chama o property , nao necessita do ()
