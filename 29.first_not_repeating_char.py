"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"" y
"""

def first_not_repeating_char(char_sequence):
    seen_letters = {} #Se crea un diccionario vacío

    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters: # si no hemos visto la letra
            seen_letters[letter] = (idx, 1) #accedemos al KEY (letter) del índice y creamos una tupla y contamos 1
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letters = []
    for key, value in seen_letters.items():
            if value[1] == 1:
                final_letters.append( (key, value[0]) ) # me crea una lista con un tupla de las letras y su índice
                #"abacabad" [(a,0),(b,1),(c,3),(d,7)]

    not_repeated_letters = sorted(final_letters, key=lambda value:value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'

if __name__=='__main__':
    char_sequence = input('Escribe una secuencia de caracteres: ')

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten')

    else:
        print('El primer caracter no repetido es {}'.format(result))
