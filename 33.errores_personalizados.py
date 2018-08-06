import os

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

def addNewContry(country):
    poblation = int(input('Cual es la poblacion de {} (en millones): '.format(country)))
    countries[country] = poblation
    print('¡Muchas gracias por tu aporte!')

while True:
    print('')
    print('')
    print('')
    print('================================================')
    print('Consulta la poblaciones de los paises del mundo')
    print('================================================')
    print('')
    country = input('Escribe el nombre de un país: ').lower()

    try:
        print('')
        print('La población de {} es de {} millones'.format(country.upper(), countries[country]))

    except KeyError:
        print('No tenemos la información de {}'.format(country))
        add = addNewContry(country)

    print('')
    print('')
    search = input('Desea realizar otra consulta? Y/N: ').upper()

    if search == 'Y':
        os.system('cls')
        True

    elif search == 'N':
        print('')
        print('')
        print('Ha sido un placer')
        break

    else:
        print('NO DATA')
        exit()
