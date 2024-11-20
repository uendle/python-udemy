import cod050 ,cod051

class Carro:
    def __init__(self, nome) -> None:
        self.nome= nome
        self._motor= None
        self._fabricante= None
    
    def exibir(self):
        print( f'{self.nome} ,motor {self._motor.nome} ,fabricante {self._fabricante.nome}')


    def set_motor (self , motor):
        self._motor = motor


    def set_fabricante (self , f):
        self._fabricante = f

        
fusca = Carro('fusca')
mot= cod050.Motor('v6')
fab= cod051.Fabricante('vw')

fusca.set_motor(mot)
fusca.set_fabricante(fab)

print(fusca.exibir())
        