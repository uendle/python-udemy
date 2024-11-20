#abstração
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def log(self, msg):
        raise NotImplementedError('implemente o metodo log')
    
class Logfile(Log):
    def log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class Logfiletxt(Log):
    def log(self, msg):
        print(msg)

if __name__=='__main__':
    obj= Logfile()
    obj.log('gravando erro no log')
    print(LOG_FILE)