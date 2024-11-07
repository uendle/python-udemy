# def fatorial(numero,con=0):
#     if con == 0:
#         con = numero
#     elif con == 1:
#         return numero
#     return fatorial(numero * con,con-1)# recursividade
    


def fatorial (numero):
    if numero == 1:
        return 1
    return numero * fatorial(numero-1)


print(fatorial(100))