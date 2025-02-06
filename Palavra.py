import os

print("bem vindo, tente acertar a palavra")


palavra = 'Futebol'

erros = 5

letras_certas = ''

palavra_formada = ''

while True:

 
    if erros == 0:
        os.system("cls")
        print('acabou suas tentativas, fim de jogo!')
        print(f'a palavra certa era {palavra.upper()}')
        break

    print(f'vc ainda tem {erros} tentativas')

    tentativa = input('coloque uma letra: ')

    if tentativa in palavra_formada:
        print("Esta letra ja foi computada")
        continue

    if len(tentativa) > 1:
        print('Digite apenas UMA letra por favor!')
        erros -= 1
        continue

    if tentativa in palavra:
        letras_certas += tentativa

    else:
        print(f'Você errou, a letra {tentativa.upper()} não tem na palavra secreta!')
        erros -= 1
        continue

    palavra_formada = ''

    for letra in palavra:
        if letra in letras_certas:
            palavra_formada += letra

        else:
            palavra_formada += '*'
        
    print(palavra_formada)
        
    if palavra_formada == palavra:
        os.system('cls')
        print('Parabéns você acertou a palavra e ganhou o jogo!')
        break



    
