import os

class Lamp: #siempre se empieza con mayuscula una clase
    # Las tres comillas se utilizan para escribir comentarios multi linea, respetando la estructura del contenido, saltos de linea espacios, etc.
    # Si observas bien, _LAMPS es una lista que tiene dos elementos de strings multi linea.
    _LAMPS = ['''            .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, _is_turned_on):  #self hace alusion a la misma instancia y la forma que vamos a manipular nuestra clase
    # __init__ constructor de la clase, el método que se ejecuta cuando se genera una nueva instancia de la clase
    #Hacemos mension a la variable ON para que se inicialice encendida.
        self._is_turned_on = _is_turned_on #primera variable privada


    def turn_on(self):  #Metodo público
        self._is_turned_on = True
        self._display_image()

    def turn_off(self): #Metodo público
        self._is_turned_on = False
        self._display_image()

    def _display_image(self): # Método privado se inicia con underscore
        if self._is_turned_on:
            print(self._LAMPS[0])

        else:
            print(self._LAMPS[1])

def run():
    lamp = Lamp(_is_turned_on = False) #igual que una funcion para inicializar una clase se ponen parentesis
    # La lista “Lamp” la guardamos es una variable, esta lista tiene el parametro “is_turned_on = False" que es la manera de decirle que cuando empiece a ejecutar todo la lampara inicialice apagada, si lo cambiaramos a True entonces estariamos diciendo que inicialice encendida

    while True:
        print('''
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
