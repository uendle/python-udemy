from log import LogPrintMixin, LogFileMixin
class Eletronico:
    def __init__(self, nome) -> None:
        self._nome = nome
        self._ligado = False

    def ligar (self):
        if not self._ligado:
            self._ligado= True
    
    def desligar(self):
        if self._ligado:
            self._ligado= False

class Smartphoe(Eletronico,LogFileMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
           msg= f'{self._nome} esta ligado.. ' 
           self.log_success(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg= f'{self._nome} esta desligado....'
            self.log_success(msg)
