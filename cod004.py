# # print(True and '' or 0 or 'abc' or True)# resultado abc 

# # nome = 'jose'
# # print(nome[0])
# # print(nome[-0])
# # if 'o' in nome:
# #     print(True)

# # print('valor = %s,valor = %d,valor = %i,valor = %.2f,valor = %x,valor = %X,valor = %04X'%('oi',1,2,3.5,15,15
# nome= 'jose'

# # print(f'{nome}')
# # print(f'{nome:x>10}')
# # print(f'{nome:x<10}')
# # print(f'{nome:x^10}')

# print(nome[1:3])
# print(nome[-3:-1])
# print(nome[0:-1:2])
# print(nome[::-1])


nome= input('Digite seu nome: ')
idade= input('Digite sua idade: ')

if nome and idade:
    print(f'seu nome e {nome}')
    print(f'seu nome invertido e {nome[::-1]}')
    print(f'seu nome {'contem' if ' ' in nome else 'nao contem'} espaços')
    print(f"seu nome tem {len(nome)}")
    print(f"a primeira letra do seu nome e {nome[0]}")
    print(f"a ultima letra do seu nome e {nome[-1]}")
else:
    print('voce deixou cmpos vazios')






