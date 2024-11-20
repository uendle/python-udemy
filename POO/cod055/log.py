from pathlib import Path

LOG_FILE = Path(__file__).parent / "log.txt"

class Log:
    def log(self, msg):#assinatura do metodo
        raise NotImplementedError('Implemente o metodo Log...')
    
    def log_error(self, msg):
        return self.log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self.log(f'Success: {msg}')
    

class LogFileMixin(Log):
    def log(self, msg):
        mensagem_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as arquivo:# modo append a mode apenas adiciona 
            arquivo.write(mensagem_formatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
    
# if __name__ == '__main__':
#     l= LogPrintMixin()
#     l.log('mensagem de log')
#     print( l.log_error('mensagem de log'))
#     l.log_success('mensagem de log')

#     l2= LogFileMixin()
#     l2.log('mensagem de log')
#     print( l2.log_error('mensagem de log'))
#     l2.log_success('mensagem de log')