import random

def randomList():
    numbers = []
    print('')
    amount = int(input('Cantidad de elementos en la lista: '))
    initNum = int(input('Límite inferior: '))
    finNum = int(input('Limite superior: '))

    for i in range(amount):
        n = random.randint(initNum,finNum)
        numbers.append(n)

    return sorted(numbers)

def ordered_list():
    disorder_list = input('Escribe una lista de numeros (al menos 10) separados por espacio: ')
    split_list = map(int, disorder_list.split(' '))

    return sorted(split_list)

def binary_search(numbers, numberToFind):
    high = len(numbers)
    if high == 0:
        return False

    mid = high//2

    if numbers[mid] == numberToFind:
        return True
    elif numbers[mid] > numberToFind:
        return binary_search(numbers[:mid-1], numberToFind)
    else:
        return binary_search(numbers[mid + 1:], numberToFind)


if __name__=='__main__':
#    numbers = randomList() #Crear una lista aleatoria. Nosotros determinamos el rango
    numbers = ordered_list() # Ingresar los números y crear lista manualmente

    print(numbers)
    print('')
    numberToFind = int(input('Escribe el número que deseas validar: '))
    result = binary_search(numbers, numberToFind)

    if result is True:
        print('')
        print('El número SI está en la lista')
    else:
        print('')
        print('El número NO está en la lista')
