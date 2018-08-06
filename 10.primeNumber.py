
def isPrime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        print("Es un número par")
        return False
    else:
        for i in range(3,number):
            if number % i == 0:  #si un número es divisible exactamente entre uno de su rango entonces no es primo.
                return False


def run():
    number = int(input("Digite un número "))
    result = isPrime(number)

    if result is False:
        print("No es un número primo")
    else:
        print ("Es número primo")

if __name__=='__main__':
    run()

#Otra forma de hacerlo es usando raíz cuadrada y lo hace de una manera más óptima
#import math

#def is_prime(n):
	#if(n<2):
	#	returnFalse
	#root=int(math.sqrt(n))
	#for a in range(2,root+1):
	#	if n%a==0:
	#		returnFalse
	#returnTrue
