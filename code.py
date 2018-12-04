import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print('Jogo da Forca By Guilherme Bromonschenkel')

# Number of rows and columns of the ambient
n_linhas = 7
n_colunas = 8

# Stick body parts
p = ['/', '\ ', '|', '/', '|','\ ', 'O']
n = len(p)

# Print the game ambient on screen
def imprimeJogo():
    linha1 = [' ', ' ', ' ', ' ', '_', '_', '_', ' ', '  ']
    linha2 = [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', '  ']
    linha3 = [' ', ' ', ' ', '|', ' ', ' ', ' ', p[6], '  ']
    linha4 = [' ', ' ', ' ', '|', ' ', ' ', p[3], p[4], p[5]]
    linha5 = [' ', ' ', ' ', '|', ' ', ' ', ' ', p[2], '  ']
    linha6 = [' ', ' ', ' ', '|', ' ', ' ', p[0], ' ', p[1]]
    linha7 = [' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '  ']
    linha8 = ['_', '_', '_', '|', '_', '_', '_', ' ', '  ']
    for k in range (n_colunas):
        print(linha1[k], end='')
        k = k + 1
    print(linha1[k])
    for k in range (n_colunas):
        print(linha2[k], end='')
        k = k + 1
    print(linha2[k])
    for k in range (n_colunas):
        print(linha3[k], end='')
        k = k + 1
    print(linha3[k])
    for k in range (n_colunas):
        print(linha4[k], end='')
        k = k + 1
    print(linha4[k])
    for k in range (n_colunas):
        print(linha5[k], end='')
        k = k + 1
    print(linha5[k])
    for k in range (n_colunas):
        print(linha6[k], end='')
        k = k + 1
    print(linha6[k])
    for k in range (n_colunas):
        print(linha7[k], end='')
        k = k + 1
    print(linha7[k])
    for k in range (n_colunas):
        print(linha8[k], end='')
        k = k + 1
    print(linha8[k])
    print('')

# Word target selection
palavra = input("-> Please type the game word target: ")
palavra = palavra.upper()
o = len(palavra)

# Tip input
dica = input("-> Please type the game tip: ")
dica = dica.upper()

# Turn the word target boxes into blank
tentativa = []
for v in range(o):
    tentativa.extend('_')

# Player's selection menu
players = input("-> Please type the total amount of players: ")
x = int(players)
player = []
for i in range(x):
        print('Player', (i+1), ': ', end='')
        player.extend([input()])
        player[i] = player[i].upper()
        i = i + 1
        if i == x:
                    print('\nLets get started!')
                    import time
                    time.sleep(1)

# Some designations
wordsSpent = ['']
count = len(wordsSpent)
vencedor = []
venceu: int = 0
l = 0
erro = 0
contador = 0

# This makes the game to work
def andamentoJogo(l):

    global contador
    global venceu

    clear_screen()
    imprimeJogo()

    print("That's the turn of [", player[l],']')
    print("- The Word Target is: ", end='')

    # Print the hidden boxes spaces on screen of Word Target
    for v in range(o):
        print(tentativa[v], ' ', end='')
    print('')

    # Session Tip
    print("- The tip for this sessions is:", dica)

    # Print all letters typed
    print("- Words Spent:", end='')
    count = len(wordsSpent)
    for i in range(count):
        print(wordsSpent[i],'', end='')

    print("\n- Try some letter: ", end='')
    wordsSpent.extend([input()])
    count = len(wordsSpent)
    # Turns all the letters typed in upper type just to eliminate some bugs
    for i in range(count):
        wordsSpent[i] = wordsSpent[i].upper()

    # This checks if the player typed the correct word
    for i in range (count):
        for j in range (o):
            if wordsSpent[i] == palavra[j]:
                tentativa[j] = wordsSpent[i]

    # This takes off the stick body part
    erro = 0
    for i in range (o):
        if wordsSpent[count - 1] != palavra[i]:
            erro = erro + 1
            if erro == o:
                p[contador] = ' '
                contador = contador + 1

    # This tries out if the player lost the game
    teste = 0
    for i in range (n):
        if p[i] == ' ':
            teste = teste + 1
            if teste == n:
                venceu = 2

    #This tries out if the player won the game
    teste = 0
    for i in range (o):
        if tentativa[i] != '_':
            teste = teste + 1
            if teste == o:
                venceu = 1
                return venceu

# The looping function that circles the game working
while venceu == 0:

    andamentoJogo(l)
    if (venceu == 1) or (venceu == 2):
        vencedor = player[l]

    #This changes the player's turn
    if l == (x-1):
        l = 0
    else:
        l = l + 1

# This shows who won or lost the game
clear_screen()
if venceu == 1:
    print('- The winner is [', vencedor, ']', 'for figuring out the word [', palavra, ']')
if venceu == 2:
    print('- The player [', vencedor, ']', 'lost the game!')
