class A:
    atributo_a= 'a'

    def metodo(self):
        print('a')

class B(A):
    atributo_b= 'b'

    def metodo(self):
        print('b')

class C(B):
    atributo_c= 'c'

    def metodo(self):
        return super(B,self).metodo()
        print('c')

obj = C()
obj.metodo()
print(C.mro())#retorna uma lista como a ordem de retorno do metodo
print(C.__mro__)#retorna uma tupla como a ordem de retorno do metodo
