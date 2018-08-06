# Curso_Python

Realice esta guía sobre los ejercicios realizados en el Curso de Python en la plataforma de Platzi
para practicar y aclarar los conceptos y lógica implementada en cada ejercicio:

[**7.0primerEjercicioCuadrado.py**](https://github.com/corozb/Curso_Python/blob/master/7.0primerEjercicioCuadro.py)

•	Hacemos uso del módulo **Turtle** para construir una gráfica: Es un módulo que permite programar gráficas de tortuga. La idea central de este tipo de gráficas consiste en desplazar un cursor (al que se le denomina tortuga) por la pantalla a partir de diferentes comandos programados. Se le llama tortuga porque normalmente la tortuga deja un rastro por el lugar donde se va desplazando.

[**7.1ejercicioCuadradoAvanzado.py**](https://github.com/corozb/Curso_Python/blob/master/7.1ejercicioCuadradoAvanzado.py)

•	Ingresamos datos con un input sobre las medidas que deseamos construir un cuadrado.
•	Definimos una función 
Las funciones son un concepto fundamental en programación, una función es una secuencia de comandos que realizan un cómputo.

En Python las funciones se definen usando la palabra reservada def y luego el nombre de la función con paréntesis y dos puntos que indican que lo que sigue son los comandos. Una función debe retornar un valor, para esto se usa la palabra reservada return.

[**7.2ejercicioCuadradoAvanzado2.0.py**](https://github.com/corozb/Curso_Python/blob/master/7.2ejercicioCuadradoAvanzado2.0.py)

Similar al código anterior, aunque en esta ocasión solicitamos la longitud de las líneas y cuantos lados debía tener la gráfica (mayor a 3)

[**7.3spiralTurtle.py**](https://github.com/corozb/Curso_Python/blob/master/7.3spiralTurtle.py)

Es un programa que crea un dibujo geométrico con una función recursiva que genera un giro y una gama de colores predeterminada.

[**8.tipo_de_cambio.py**](https://github.com/corozb/Curso_Python/blob/master/8.tipo_de_cambio.py)

Consiste en un ejercicio que lo que hace es la conversión de una moneda en otra. En este caso pasa de COP a MXN.

Vemos:
- Declarar variables 
- Uso de funciones matemática dentro de Python 
-	Imprimir variables
-	Crear funciones

Límites al declarar funciones:
-	Los nombres no pueden comenzar con dígitos
-	No pueden utilizar una palabra reservada
-	Las variables deben tener diferentes nombres
-	Los nombres de las funciones deben ser descriptivas de lo que hacen las funciones

Imprimir valor de variable
Para poder imprimir el valor de una variable dentro de un string podemos hacerlo así:

`'${} pasos mexicanos son ${} pesos mexicanos'.format(amount, result)`

[**10.primeNumber.py**](https://github.com/corozb/Curso_Python/blob/master/10.primeNumber.py)

Un programa que nos permite determinar si un número es primo o no, usando:
- Expresiones booleanas, 
-	Operadores relacionales y 
-	Operadores lógicos.

[**13.factorialNumber.py**](https://github.com/corozb/Curso_Python/blob/master/13.factorialNumber.py)

Función Recursiva: cuando dentro del bloque de instrucciones que la conforma se usa a sí misma, p.e. cuando haces el cálculo de la factorial de un número lo haces con una función recursiva:

La factorial de un número es el número multiplicado por los números antes de él, por ejemplo 

                          5! es 5x4x3x2x1 = 120
**Nota importante:** Cuándo se esté trabajando con recursividad siempre pensar en el caso base, es decir definir el momento en el que la función dejará de llamarse a sí misma, para que haga un loop infinito, por ejemplo, en el caso de la factorial termina la ejecución cuando llega a cero.

[**17.randomNumberFind.py**](https://github.com/corozb/Curso_Python/blob/master/17.randomNumberFind.py)

El juego consiste en dar un rango de número en el cual debes adivinar el número que escogió la computadora.

Otra forma de hacer iteraciones es con el **while loop**, éste ciclo se ejecuta MIENTRAS la condición se evalúe como **verdadera**, el ciclo termina cuando la evaluación resulta en falso.

En este tipo de ciclo es muy importante definir la condición de parada, si no el ciclo puede ejecutarse hasta el infinito y consumir todos los recursos de la máquina.

Recuerda:
-	Para detener la ejecución de un ciclo, puede utilizar `CTRL + C` en la consola

[**18.0invertirPalabrasRANGE.py**](https://github.com/corozb/Curso_Python/blob/master/18.0invertirPalabrasRANGE.py)

Creamos un programa al cual le ingresamos una palabra y nos arroja como resultado la misma de forma invertida. 

[**18.1palindromoInvertir.py**](https://github.com/corozb/Curso_Python/blob/master/18.1palindromoInvertir.py)

Basados en el programa anterior creamos un programa para saber si una palabra es un palíndromo. Un palíndromo es una frase o palabra que dice lo mismo al derecho y al revés.

[**19.0calculoPromedios.py**](https://github.com/corozb/Curso_Python/blob/master/19.0calculoPromedios.py)

Conocemos el uso de **listas** y creamos un programa para el calculo de promedios. 
Una lista es una secuencia de elementos, para crearlas usamos corchetes `[]` o con la función `list`.

[**19.1promedioNotas.py**](https://github.com/corozb/Curso_Python/blob/master/19.1promedioNotas.py)

Basado en el ejercicio anterior construí un programa para averiguar si el promedio de cada estudiante le daba para ganar el semestre de la universidad.

[**23.ahorcadoGame.py**](https://github.com/corozb/Curso_Python/blob/master/23.ahorcadoGame.py)

El juego consiste en adivinar palabras ingresando letra por letra, inicialmente lo que haremos es mostrar el tablero del juego y pedir al usuario que ingrese una letra, si la letra está contenida en la palabra aleatoria del juego se agregará a la lista en caso contrario de mostrará una nueva parte del ahorcado indicando que ese intento fue fallido. 

En este ejercicio hacemos uso de:
-	Loops
-	Manejo de listas y agregar datos a ella

Igualmente conocí el módulo **random** que nos facilita la forma de escoger un elemento aleatorio entre una lista.

[**25.binary_search.py**](https://github.com/corozb/Curso_Python/blob/master/25.binary_search.py)

Un programa que realiza una búsqueda binaria de un número dentro de una lista y nos valida si un número se encuentra o no en ella.

La **búsqueda binaria** es un algoritmo eficiente para encontrar un elemento en una lista ordenada de elementos. Funciona al dividir repetidamente a la mitad la porción de la lista que podría contener al elemento, hasta reducir las ubicaciones posibles a solo una.

[**27.cypherWords.py**](https://github.com/corozb/Curso_Python/blob/master/27.cypherWords.py)

Un programa, a modo de juego, para poder cifrar un mensaje con un código “secreto” para que el receptor, quien a su vez tiene la clave del código, lo pueda descifrar. 

Usamos:
-	Diccionarios
-	Join
-	Split

[**29.first_not_repeating_char.py**](https://github.com/corozb/Curso_Python/blob/master/29.first_not_repeating_char.py)

Construimos un programa que nos permite encontrar el primer carácter que no se repite en un `string`.

Por ejemplo, si tenemos el string `‘mimamameama’` el primer carácter que no se repite es la `i`.

Para esto hacemos uso de **Tuplas**.

[**33.errores_personalizados.py**](https://github.com/corozb/Curso_Python/blob/master/33.errores_personalizados.py)

Este programa realizamos consultas en un diccionario donde las llaves serán los países y el valor será la población de dichos países (en millones).

Partimos de un diccionario base, pero también podemos agregarle los datos de países que estamos consultando.

Vamos a ver un método para **encapsular un error**. Cuando el programa no sabe como hacer algo lanza una alerta. **Try** y **except** son las palabras reservadas que utiliza Python para solucionar problemas de errores que no queremos que nos cierre el programa, el error se encapsula entre esas dos palabras.

```

try:
     Código a ejecutar
except:
     Código para recibir el error y hacer algo

else: 
    Código cuando el try si funcione y No ejecute el except

finally:
    Código que siempre se ejecutará, independientemente de except o else
```

[**34.leer_archivos.py**](https://github.com/corozb/Curso_Python/blob/master/34.leer_archivos.py)

Este programa permite traer un archivo a Python y manipularlo desde allí. Por ejemplo, contar la cantidad de veces que una palabra aparece en dicho archivo.

-	Python puede leer y escribir archivos con la función **open**.
-	La función **open** regresa un objeto archivo (file)
-	Los archivos pueden ser textos o binarios
-	Se tiene que especificar el modo en que se maneja el archivo:
    ‘r’ = read
    ‘w’ = write
    ‘a’ = append
    ‘r+’ = read and write
-	Se debe cerrar el archivo con el método **close** para evitar pérdidas de información
-	La mejor manera de manejar archivos es con la keyword **with** que se maneja cuando algunas funciones van en par:
   			          `Open-close`

[**36.classLamp.py**](https://github.com/corozb/Curso_Python/blob/master/36.lampara/36.classLamp.py) - [**main.py**](https://github.com/corozb/Curso_Python/tree/master/36.lampara) - [**36.classVehiculo.py**](https://github.com/corozb/Curso_Python/blob/master/36.classVehiculos.py)

Programación Orientada a Objetos.

**Clase:** Modelo donde se redactan las características comunes de un grupo de objetos. Ejemplo, chasis carro con cuatro ruedas
**Instancia:** Ejemplar perteneciente a una clase. Ejemplo, El tipo de llantas, sillas, color, etc.
**Métodos:** Los métodos son como funciones que tienen sentido sólo en el contexto de una clase. Ejemplo, Clase: Carro métodos: Arrancar, acelerar, frenar.
	                Clase: Lampara método: prender, apagar, salir

[**37.decorador_protegida.py**](https://github.com/corozb/Curso_Python/blob/master/37.decorador_protegida.py)

La idea de este programa es la ejecución de una función que está protegida por una contraseña: orozco

Un decorador es una función que recibe otra función y regresa una tercera función. En servidores web existen funciones que nada más deben ejecutarse si un usuario se encuentra autenticado. 

Para reconocer un decorador, se tiene una arroba **(@)** sobre la declaración de una función.

[**40.web_scraping.py**](https://github.com/corozb/Curso_Python/blob/master/40.web_scraping/40.web_scraping.py)

Web scraping es una herramienta que permite visitar sitios web, analizar su contenido y obtener información. Este programa ingresa a la página web (https://xkcd.com) y descarga la cantidad de imágenes que deseemos con su nombre original.

Usaremos dos librerías: 
-	**Requests:** Permite hacer solicitudes a un sitio web y traer cualquier contenido que se pueda transferir a través de internet, puede ser: .html, .xml o .json
-	**Beautifulsoap:** Permite analizar documentos HTML. Esta biblioteca crea un árbol con todos los elementos del documento y puede ser utilizado para extraer información. 

[**42.contacts.py**](https://github.com/corozb/Curso_Python/blob/master/42.contacts_command/42.contacts.py)

Vamos a crear un programa que sea una agenda de contactos, para esto debemos pensar, ¿qué es realmente una agenda?

Una agenda es un agrupador de contactos que nos permite añadir, eliminar y ver contactos.
Aseguramos también la **persistencia de los datos** grabando la información de los contactos en el disco duro de nuestro equipo.

[**Red Social:**](https://github.com/corozb/Curso_Python/blob/master/Red_Social/socialNetwork.py) 
Este programa es una red social en la cual podemos agregar contactos, publicar mensajes y enviarlo a los contactos que deseemos. Este programa también tiene la propiedad de persistencia de los datos. Fue realizado como material de estudio del curso de Python dictado por la Universidad Católica de Chile a través de coursera.org. Contiene los datos de 3 usuarios:
-	Cristian
-	Brandon
-	Oliver

**Desafíos:**
Al finalizar el curso se deben cumplir con tres desafíos para practicar nuestros conocimientos. 
- [**Desafío 1:**](https://github.com/corozb/Curso_Python/blob/master/desafio1SumaRecursiva.py)  Crear una función que sume recursivamente
- [**Desafío 2:**](https://github.com/corozb/Curso_Python/blob/master/desafio2CryptoBinarios.py) Criptografía con binarios. Crear nuestro código de encriptación con el sistema binario 
- [**Desafío 3:**](https://github.com/corozb/Curso_Python/blob/master/desafio3CreaObjeto/main.py) Modelar un Objeto
