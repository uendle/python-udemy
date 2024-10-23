import os

palavra_secreta= 'uendle'
tentativa = 0
chute= ''
palavra= ''
temp=''
os.system('clear')
while True:
   
    tentativa+=1
    letra= input(f'Digite apenas uma letra tentativa {tentativa} : ') or None
    chute=''
    temp=''
  

    if letra is None:
        print('Digiet apenas uma letra!!!')
        continue

    elif len(letra) > 1:
        print('Digiet pelo menus uma letra!!!')
        continue


    for i in palavra_secreta:
        if i == letra :
            chute += i
        else :
            chute += '*'
    
    for i in range(len(palavra_secreta)) :
        if palavra == '':
            palavra = chute
        if palavra[i] == '*':
            temp+= chute[i]
        else:
            temp+= palavra[i]

    os.system('clear')
    palavra= temp
    print('\n',palavra)

    if palavra_secreta == palavra:
        print(f'parebens voçe acertou com {tentativa} tentativas a palavra {palavra}')
        break
    
    