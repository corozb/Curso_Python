def recursiva(number):
    if number == 0:
        return 0
    else:
        suma = 0
        for i in range(number+1):
            suma += i
        print('El resultado de la suma recursiva de los numero de 1 a {} da como resultado {}'.format(number, suma))

if __name__=='__main__':
    number = int(input("Ingresa un número para saber su suma recursiva: "))
    result = recursiva(number)
