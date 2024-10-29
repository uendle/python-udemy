def multiplicar (*args):
    total= 1
    for iten in args:
        total*= iten
    return total

def epar(valor):
    return valor % 2 == 0
    # if valor % 2 ==0:
    #     return True
    # return False

s=multiplicar(2,4,6,4)
print(s)

print(epar(s))