# valor= input('Digite um valor : ')

# if valor.isdigit():#verifica se e um numero inteiro
#     print(f'o dobro de {valor} e {int(valor) * 2}')
# else:
#     print('Lamento isso não e um numero valido!!!!')


# try:
#     valor_float= float(valor)
#     print(f'valor : {valor}')
# except:
#     print('Ocorreu um erro estamos no except!!!!')






# numero= input('Digite um numero inteiro')
# if numero.isdigit():
#     resultado= int(numero)% 2 
#     if resultado == 0:
#         print('nuero par')

#     else:
#             print('Numero impar!')

# else:
#     print('voce não digitou um numero inteiro')







# try:
#     hora= int(input('Digite a hora: '))

#     bom_dia= hora >= 0 and hora <= 11
#     boa_tarde= hora >= 12 and hora <= 17
#     boa_noite= hora >= 18 and hora <= 23

#     if bom_dia:
#         print('Bom dia!!')
#     elif boa_tarde:
#         print('Boa tarde!!')
#     elif boa_noite:
#         print('Boa noite!!!')
#     else:
#         print('hora invalida!!!')
# except:
#     print('Apenas numeros inteiros serao aceitos!!!')





nome= input('Digite seu primeiro nome: ')

if nome.isdigit():
    print('voce digitou um numero')
else:
    nome_curto= len(nome) <= 4
    nome_grande= len(nome) > 6
    nome_comum= not(nome_curto and nome_grande) 

    if nome_curto:
        print(f'seu nome e curto .')
    elif nome_grande:
        print(f'seu nome e grande .')
    elif nome_comum:
        print(f'seu nome e comum .')