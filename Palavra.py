import os
import random 

categorias = { 
    'esporte': ['futebol','basquete','volei','nataçao','tenis'],
    'animais': ['cachorro','gato','jacare','elefante','girafa'],
    'frutas': ['maça','banana','pera','maracuja','melancia'],
    'cozinha': ['garfo','faca','panela','prato','fogao']
}

def selecionar_palavra():
   
    while True:
     
     for i,categoria in enumerate(categorias,1):
        print(f'{i}) {categoria}')
        print()
     try:
      escolha = int(input("digite a categoria que deseja: "))

      if not escolha:

        print("a categoria não pode ser vazia!")
        continue
     
      lista = list(categorias.keys())

      categoria_escolhida = lista[escolha-1] 

      palavra_escolhida = random.choice(categorias[categoria_escolhida])

      print(f'Categoria escolhia: {categoria_escolhida}')

      return palavra_escolhida
     except ValueError:
        print("Digite um indice valido")

     
def limpar_tela():
   os.system('cls' if os.name == 'nt' else 'clear')   


def menu():
    limpar_tela()
    print("---Bem vindo, tente acertar a palavra---")
    print()
    
def jogo(palavra):
   letras_certas = set()
   erros = 5

   while True:
      
      if erros == 0:
         limpar_tela()
         print(f"""-----Fim de jogo-----
 A palavra certa era:
       {palavra}
---------------------""")
        
         break
      
      tentativa = input("Digite sua tentativa: ").lower().strip()

      if len(tentativa) > 1:
         print("Digite apenas 1 letra!")
         continue
      
      if tentativa in letras_certas:
         print("Esta letra ja foi computada")
         continue
      
      if tentativa in palavra:
         print("Parabéns, acertou a letra")
         letras_certas.add(tentativa) 
      else:
         print('Você errou a letra!')
         erros -= 1
      palavra_formada = ''
      for letra in palavra:
           if letra in letras_certas:
              palavra_formada += letra
           else:
                palavra_formada += "*"

      print(palavra_formada)

      if palavra_formada == palavra:
         limpar_tela()
         print(f"""----Parabéns você ganhou o jogo!----
        A palavra era:
            {palavra}
 -----------------------------------""")
         break
      
      print(f'Você ainda tem {erros} tentativas!')


menu()
palavra = selecionar_palavra()
jogo(palavra)


