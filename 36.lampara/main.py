import os
from lamp import Lamp

def run():
    lamp = Lamp(_is_turned_on = False)

    while True:
        print('''
            Aquí puedes manipular una lámpara, tienes varias opciones:

                [p]render
                [a]pagar
                [s]alir
        ''')
        print('')
        command = input('¿Qué deseas hacer?: ')

        if command == 'p':
            os.system('cls')
            lamp.turn_on()

        elif command == 'a':
            os.system('cls')
            lamp.turn_off()
        else:
            os.system('cls')
            break

if __name__=='__main__':
    run()
