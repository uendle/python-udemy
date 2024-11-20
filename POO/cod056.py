class MeuError(Exception):
    ...
class MeuOutroError(Exception):
     ...

def levantar():
    exception_ = MeuError('A mensegem do meu erro...','so BO')
    exception_.add_note('******nota extra *********')
    exception_.add_note('******nota extra *********')

    raise exception_

try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)

    exception_ = MeuOutroError('lançando outro erro....')

    exception_.__notes__= error.__notes__.copy()#copia a  nota do outro exception
    exception_.add_note('_________outra nota extra_________')
    exception_.add_note('_________outra nota extra_________')
    raise exception_ from error
