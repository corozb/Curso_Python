import os

binary_base = [1, 2, 4, 8, 16, 32, 64, 128]

def cypher(message):
    cypher_words = [] #Se crea una lista vacía
    for letter in message:
        cypher_letter = format( ord(letter), 'b' )
        cypher_words.append(cypher_letter) #Agregamos a la lista creada

    return' '.join(cypher_words) # por cada espacio empieza una nueva palabra y unir a la lista


def decipher(message):
    words = message.split(' ')
    decipher_message = []

    for word in words:
        word = str(word) #lo convertimos en string
        sumatory = 0
        for value, letter in enumerate(word[::-1]): #en orden inverso
            if int(letter) == 1:
                sumatory += binary_base[value]
        decipher_letter = chr(sumatory)
        decipher_message.append(decipher_letter)

    return ' '.join(decipher_message)


def run():

    while True:

        print('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        ''')
        print('')
        command = str(input('Ingrese una opción: '))
        print('')

        if command == 'c' or command == 'C':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print('Mensaje cifrado...')
            print('{}'.format(cypher_message))
            print('')

        elif command == 'd'or command == 'D':
            message = str(input('Escribe tu mensaje cifrado: '))
            decipher_message = decipher(message)
            print('Mensaje descifrado...')
            print('{}'.format(decipher_message))
            print('')

        elif command == 's'or command == 'S':
            print('BYE :(')
            os.system('cls')
            print('')
            break
        else:
            print('¡Comando no encontrado!')

if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()
