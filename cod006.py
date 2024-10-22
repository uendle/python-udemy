# nome = input('Digite seu nome : ')
# nome_diferente= '*'
# i=0
# while i < len(nome) :
#     nome_diferente += (nome[i] + '*')
#     i+= 1
    
# print(nome_diferente)


while True:
    operacao = input('digite a operaçao [+|-|/|*]:')
    valor1= float(input('Digite um primeiro valor: '))
    valor2= float(input('Digite um segundo valor: '))

    if operacao == '+':
        print(f'a soma de {valor1:.0f} + {valor2:.0f} = {valor1 + valor2}')

    elif operacao.startswith('-'):#começa com 
        print(f'a subtraçao de {valor1:.0f} - {valor2:.0f} = {valor1 - valor2}')

    elif operacao.endswith('/'):#termina com 
        print(f'a divisão de {valor1:.0f} / {valor2:.0f} = {valor1 / valor2}')

    elif operacao == '*':
        print(f'a multiplicaçao de {valor1:.0f} X {valor2:.0f} = {valor1 * valor2}')
    else:
        print('Valor invalido')