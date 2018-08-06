
def palindrome():
    word = input('Ingresa una palabra: ')

    if word == word[::-1]: #selecciona los elementos de la lista en forma invertida
        print('La palabra {} es un palindromo'.format(word.upper()))
    else:
        print('{} no es un palindromo'.format(word.upper()))


if __name__=='__main__':
    palindrome()
