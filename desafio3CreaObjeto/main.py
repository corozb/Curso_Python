import os
from car import Car

def run():
    car = Car(_is_running_off = False)

    while True:
        print('''
            Tienes varias opciones
                [p]arqueo
                [a]celerar
                [m]axima velocidad
                [s]alir
        ''')
        print('')
        command = input('¿Que deseas hacer?: ')

        if command == 'p':
            os.system('cls')
            car.running_off()
            print('Que lindo mi carro')

        elif command == 'a':
            os.system('cls')
            car.running_on()
            print('Arranquemos pues')

        elif command == 'm':
            os.system('cls')
            car.max_speed()
            print('Maneja con precaución')

        else:
            os.system('cls')
            break

if __name__=='__main__':
    run()
