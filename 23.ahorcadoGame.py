import random
import os

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS =[
'langosta',
'pizza',
'portatil',
'mouse',
'camino',
'teclado'
]

def randomWord():
    idx = random.randint(0, len(WORDS)-1)
    #un índice aleatorio entre 0 y la longitud de la lista WORDS. (-1) porque son 6 elementos en lista y los índices son de 0 - 5.
    return WORDS[idx]
# otra forma más simple
#   return random.choice(WORDS)

def display_board(hiddenWord, tries):
    print(IMAGES[tries])
    print('')
    print(hiddenWord)
    print('')
    print('--- * --- * --- * --- * --- * --- * --- * ---')

def run():
    word = randomWord()
    print('')
    print('Es una palabra de {} letras'.format(len(word)))
    hiddenWord = ['-'] * len(word) # creamos una lista vacía con '_' que se repetirá tantas veces como letras tenga la palabra elegida aletoriamente en randomWord()
    tries = 0 # este irá incrementando y nos ubicará en IMAGES a cada falla

    while True:
        display_board(hiddenWord, tries)
        letra = input('Escoge una letra: ')
        current_letter = letra.lower()
        os.system('cls')

        letter_indexes = []
        for idx in range (len(word)):
            if word[idx]== current_letter: #verifica si en el indice es igual a la letra actual y la agrega

                letter_indexes.append(idx)

        if len(letter_indexes)==0:
            #valida si agregó letra a la lista sino suma un intento
            tries += 1

            if tries == 6:
                display_board(hiddenWord, tries)
                print('')
                print('¡¡¡SORRY YOU LOST!!!')
                print('The right words was: {}'.format(word.upper()))
                print('')
                break
        else:
            for idx in letter_indexes:
                hiddenWord[idx] = current_letter
                # si no está vacía reemplazamos '-' por la letra que ingresamos
            letter_indexes = [] # dejamos la lista nuevamente vacía y empezamos otra vez

        if not '-' in hiddenWord:
            print('')
            print('¡¡GREAT YOU WIN!! The word is: {}'.format(word.upper()))
            break



#        try:
#            hiddenWord.index('-')  #Buscamos si hay algún guión en la lista
#        except ValueError:
#            print('')
#            print('¡¡GREAT YOU WIN!! The word is: {}'.format(word))
#            break

if __name__=='__main__':
    print('')
    print('*-_-*-_-*_-*-_-*_-*-_-*_-*-_-*_-*-_-*')
    print('* J U E G O  D E L  A H O R C A D O *')
    print('*-_-*-_-*_-*-_-*_-*-_-*_-*-_-*_-*-_-*')
    print('')
    print('Adivina la palabra antes de ser ahorcado')
    run()
