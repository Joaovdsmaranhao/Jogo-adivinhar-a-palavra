
# Jogo da Forca em Python

Um projeto simples e interativo de um **Jogo da Forca** desenvolvido em Python. Este jogo permite aos usuários selecionar uma categoria de palavras e tentar adivinhar a palavra secreta letra por letra, com um número limitado de tentativas.

---

## Funcionalidades

* **Seleção de Categoria Dinâmica:** O jogo apresenta uma lista de categorias pré-definidas, permitindo ao usuário escolher o tema da palavra a ser adivinhada.
* **Mecanismo de Jogo Interativo:** Implementa a lógica clássica do jogo da forca, com feedback visual sobre letras corretas e incorretas.
* **Gerenciamento de Tentativas:** Os jogadores têm um número fixo de tentativas (5 erros) antes que o jogo termine.
* **Limpeza de Tela:** Funcionalidade para limpar o console, garantindo uma experiência de usuário mais limpa a cada turno.

---

## Como Rodar o Projeto

Para executar este jogo no seu ambiente local, siga os passos abaixo:

1.  **Pré-requisitos:** Certifique-se de ter o **Python 3.x** instalado em sua máquina.

2.  **Clone o Repositório (se aplicável):** Se este código estiver em um repositório, clone-o para o seu ambiente local:

    ```bash
    git clone https://github.com/Joaovdsmaranhao/Jogo-adivinhar-a-palavra
    cd Jogo-adivinhar-a-palavra
    ```

3.  **Execute o Script:** Navegue até o diretório onde o arquivo `forca.py` está salvo e execute-o via terminal:

    ```bash
    python Jogo-adivinhar-a-palavra.py
    ```

---

## Como Jogar

Após iniciar o jogo, você será guiado pelas seguintes etapas:

1.  **Escolha da Categoria:** Uma lista numerada de categorias será exibida. Digite o número correspondente à categoria desejada e pressione `Enter`.
2.  **Tentativas de Letra:** O jogo exibirá a palavra oculta usando asteriscos (`*`) para as letras desconhecidas. Digite uma única letra por vez e pressione `Enter` para submeter sua tentativa.
3.  **Feedback e Progresso:** O sistema informará se a letra está na palavra. Letras corretas serão reveladas na palavra oculta, enquanto letras incorretas reduzirão seu contador de tentativas.
4.  **Condições de Fim de Jogo:**
    * **Vitória:** Ocorre quando todas as letras da palavra são corretamente adivinhadas.
    * **Derrota:** Ocorre quando o número de tentativas esgota. A palavra correta será revelada.

---

## Estrutura do Código

O código é modularizado em funções para clareza e manutenção:

* `categorias`: Um dicionário Python que armazena as categorias e suas respectivas listas de palavras.
* `selecionar_palavra()`: Responsável por exibir as categorias, permitir a seleção do usuário e retornar uma palavra aleatória da categoria escolhida.
* `limpar_tela()`: Utiliza o módulo `os` para limpar o console, garantindo uma experiência de usuário sem sobrecarga de texto.
* `menu()`: Exibe a mensagem de boas-vindas do jogo.
* `jogo(palavra)`: Contém a lógica principal do jogo, gerenciando as tentativas do jogador, o feedback das letras e as condições de vitória/derrota.

---

## Personalização

Você pode facilmente estender ou modificar as categorias e palavras existentes no jogo. Basta editar a variável `categorias` no arquivo `forca.py` conforme suas preferências:

```python
categorias = {
    'esporte': ['futebol','basquete','volei','nataçao','tenis'],
    'animais': ['cachorro','gato','jacare','elefante','girafa'],
    'frutas': ['maça','banana','pera','maracuja','melancia'],
    'cozinha': ['garfo','faca','panela','prato','fogao']
}
```

---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** para relatar bugs ou sugerir melhorias, ou submeter **pull requests** com novas funcionalidades ou otimizações.

---
