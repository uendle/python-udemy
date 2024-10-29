import re


cpf=input(' Digite seu CPF: ').replace('.','')
contador= 10
decimo_digito= 0
ultimo_digito= 0

for d in cpf:
    if d == '-':
        break
    else:
        decimo_digito += (int(d) * contador)
        contador-= 1

decimo_digito *= 10
resto = decimo_digito % 11
decimo_digito = 0 if resto > 9 else resto




# cpf = cpf.replace('-','')
cpf= re.sub(r'[^0-9]','',cpf)#expressao regular 
dez_digitos = cpf[:10]
contador= 11


for d in dez_digitos:
    ultimo_digito += (int(d)* contador)
    contador-= 1

ultimo_digito *= 10
ultimo_digito= ultimo_digito % 11
ultimo_digito = 0 if ultimo_digito > 9 else ultimo_digito
print('-',decimo_digito,ultimo_digito,sep='')
    