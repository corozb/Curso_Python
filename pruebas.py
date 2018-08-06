import os

class Car:
    _CAR = ['''
   -
                     \
      __________ ___/_>________
     /  ____ \ <>     |  ____  \
    =\_/ __ \_\_______|_/ __ \__D
________(__)_____________(__)____
    ''',
    '''
       -           __
 --          ~( @\   \
---   _________]_[__/_>________
     /  ____ \ <>     |  ____  \
    =\_/ __ \_\_______|_/ __ \__D
________(__)_____________(__)____
''',
'''
   o_______________}o{
   |              |   \
   |    911       |____\_____
   | _____        |    |_o__ |
   [/ ___ \       |   / ___ \|
  []_/.-.\_\______|__/_/.-.\_[]
     |(O)|             |(O)|
      '-'   ScS         '-'
---   ---   ---   ---   ---   ---
''']

def __init__(self, _is_running_off):
    self._is_running_off = _is_running_off

def running_off(self):
    self._is_running_off = True
    self._display_image()

def running_on(self):
    self._is_running_on = False
    self._display_image()

def max_speed(self):
    self._is_max_speed = False
    self._display_image()

def _display_image(self):
    if self._is_running_off:
        print(self._CAR[0])

    elif self._is_running_on:
        print(self._CAR[1])

    else:
        print(self._CAR[2])

def run():
    car = Car(_is_running_off = False)

    while True:
        print('''
            Tienes varias opciones
                [p]arqueo
                [a]celear
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
