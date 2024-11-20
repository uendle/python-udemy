class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
    
class ferramenta_de_escrever:
    def __init__(self, nome):
        self.nome= nome

    def escrever(self):
        return f'{self.nome} esta escrevendo...'

escritor = Escritor('jose')
lapis = ferramenta_de_escrever('lapis')
caneta= ferramenta_de_escrever('caneta')

escritor.ferramenta= lapis
print(escritor.ferramenta.escrever())
print(lapis.escrever())

escritor.ferramenta= caneta
print(escritor.ferramenta.escrever())
print(lapis.escrever())