# x = 1

# def soma(a,b):
#      #global x
#      x= a+b
#      def imprimir():
#           print(x)
#      imprimir()
# soma(2,2)
# print(x)

#______________________________


# def retorno(a,b):
#         return a, b

# for i in retorno(1,2):
#         print(i)
# print(type(retorno(3,4)))

#______________________________


def imprime(*args):
    print(args, type(args))

imprime(1,2,3,4,5,6,7,78)