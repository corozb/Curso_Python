import random
import os

def rango():
    print("=====================================================")
    print("..........VAMOS A ADIVINAR EL NUMERO.................")
    print("=====================================================")
    print('El juego consiste en dar un rango de número en el cual debes adivinar el número que escogió la computadora')
    print('Primero debemos determinar el rango en el que debemos adivinar el número. Entonces será un número')
    numberInit = int(input('entre '))
    numberEnd = int(input('y el número '))
    print("")
    randomNumber = random.randint(numberInit,numberEnd) #crear numeros enteros  aleatorio entre 0 -20
    return randomNumber

def run():
    os.system('cls') # clear console
    number_found = False
    randomNumber = rango() #Se invoca la funcion donde se encuentra la variable

    while not number_found:
        number = int(input('Adivina el número: '))
        print("")


        if number == randomNumber:
            os.system('cls') # clear console
            print('=================================')
            print('****         QUE BIEN!!!     **** ')
            print('****  Encontraste el Número! ****')
            print('=================================')
            print("")
            print("")
            retry = input("¿Quieres jugar de nuevo? (Y/N): ")
            if retry[0].upper()=="Y":
                os.system('cls') # clear console
                randomNumber = rango()
                number_found = False
            else:
                os.system('cls') # clear console
                number_found = True
        elif number < randomNumber:
            print('El número es mas grande')
        else:
            print('El número es más pequeño')

if __name__=='__main__':
    run()
