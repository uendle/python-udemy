nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura(METROS): '))
peso= float(input('Digite seu peso(KG): '))
imc = peso/(altura**2)

print(f'{nome} tem {altura} de altura,')
print(f'pesa {int(peso)} e seu IMC é ')
print(f'{imc:.2f}','precisa procurar ajuda ' if imc > 25 or imc < 18 else 'parabens seu peso esta ok!!')
