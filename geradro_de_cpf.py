import random

cpf=""
decimo_digito =0
decimo_primeiro_digito=0
cont = 10
valor=0

for i in range(9):
   cpf+= str(random.randint(0,9))

for i in cpf:
    valor+= int(i) * cont
    cont -= 1
valor*= 10
valor%=11
cpf+=str(0 if valor > 9 else valor)


cont=11
valor=0

for i in cpf:
    valor+= int(i) * cont
    cont-= 1

valor*= 10
valor%= 11
cpf+= str(0 if valor > 9 else valor)




print(f'CPF gerado ({cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]})',cpf,sep=' --> ')