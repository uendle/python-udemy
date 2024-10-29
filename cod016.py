import os
perguntas = [
    {
        'pergunta':'quanto e 2 + 2?',
        'opções':['1','3','4','5'],
        'resposta':'4',
    },
        {
        'pergunta':'quanto e 5 + 5?',
        'opções':['10','3','4','5'],
        'resposta':'10',
    },
        {
        'pergunta':'quanto e 2 - 2?',
        'opções':['1','0','4','5'],
        'resposta':'0',
    },
]
acerto = 0 
erros= 0

for dicionario in perguntas:
    print(dicionario['pergunta'])
    for indice , opções in enumerate(dicionario['opções']):
        print(indice,') ',opções)

    chute = int(input('==>'))
    if dicionario['opções'][chute] == dicionario['resposta']:
        os.system('clear')
        print('parabens voçe acertou👍🏻!!!')
        acerto+= 1

    else:
        os.system('clear')
        print('Que pena não foi dessa vez😥!!!')
        erros+=1

if acerto == len(perguntas):
    print(f"Voce Acertou todas as {acerto} perguntas🤩")
else:
    print(f'Voce acertou {acerto} perguntas e errou {erros} !!')