from datetime import datetime

nome = input('digite seu nome: ')
sobrenome= input('Digite seu sobrenome: ')
ano_nascimento = datetime.strptime(input("digite o ano de nascimento(dia/mes/anoano): "),"%d/%m/%Y")
idade= int(datetime.now().year - ano_nascimento.year)
maior_idade = True if idade > 18 else False
altura_metros= float(input('Digite sua altura: '))

print('Nome: ',nome)
print('Sobrenome: ',sobrenome)
print('Idade: ',idade)
print('Ano de nascimento: ',ano_nascimento.year)
print('E maior de idade: ',maior_idade)
print('Altura em metros: ',altura_metros)