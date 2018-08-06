#Hola
#Ahora que ya conocemos como utilizar listas, podemos agregar una funcionalidad mucho más interesante
#a nuestra red social, y que nos hacía falta: administrar listas de amigos y de mensajes

#La segunda característica será la publicación de un muro.


# se  importa el archivo que tiene las funciones#
import funcionesRed as funcion

funcion.bienvenida()
nombre = funcion.obtener_nombre()
print("Hola ", nombre, ", bienvenido a NetWork")

#Verificamos si el archivo existe
if funcion.existe_archivo(nombre+".user"):
    #Esto lo hacemos si ya había un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, apellido, sexo, edad, ciudad, estatura_m, estatura_cm, amigos, estado, muro) = funcion.leer_usuario(nombre)

else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo haciamos antes
    print()
    apellido = funcion.obtener_Apel()
    sexo = funcion.obtener_sexo()
    edad = funcion.obtener_edad()
    ciudad = funcion.obtener_ciudad()
    (estatura_m, estatura_cm) = funcion.obtener_estatura()

    # La lista de mensajes reemplazará a nuestro antiguo valor "num_amigos". Al conocer la lista de amigos,
    # también conoceremos la cantidad de amigos. Observa cómo leemos la lista de amigos en la función
    # obtener_lista_amigos.
    #num_amigos = funcion.obtener_num_amigos()
    amigos = funcion.obtener_lista_amigos()
    estado = ""
    # Hemos agregado dos valores nuevos para el perfil del usuario: una lista de amigos, y una lista de mensajes
    # que llamaremos "muro"
    muro =[]

#En ambos casos, al llegar aquÃ­ ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
funcion.mostrar_perfil(nombre, apellido, sexo, edad, ciudad, estatura_m, estatura_cm, amigos)
funcion.mostrar_mensaje(nombre, estado)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = funcion.opcionMenu()
    # Código para la opción 1. Publicar un mensaje.
    if opcion == 1:
        estado = funcion.pubMensaje()
        funcion.publicar_mensaje(nombre, amigos, estado, muro)

    # Código para la opción 2. Publicar un mensajes a un grupo de personas.
    elif opcion == 2:
    # En el archivo de cada usuario, luego de escribir su estado actual, agregaremos una lista de los mensajes
    # que han sido publicados por sus amigos, de manera de formar una lista de mensajes que llamaremos "muro", o 'timeline',
    # presente en casi todas las redes sociales.
        funcion.mostrar_muro(muro)
        #estado = funcion.pubMensaje()
        #for i in range(num_amigos):
        #    nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
        #    funcion.mostrar_mensaje(nombre, nombre_amigo, estado)

    # Código para la opción 3. Publicar los datos del perfil del usuario.
    elif opcion == 3:
        funcion.mostrar_perfil(nombre, apellido, sexo, edad, ciudad, estatura_m, estatura_cm, amigos)

    # Código para la opción 4. Actualizar los datos del perfil del usuario.
    elif opcion == 4:
        actualizar = True
        while actualizar:
            select = funcion.actualizar_datos()
            if select == 1:
                nombre = funcion.obtener_nombre()
            elif select == 2:
                apellido = funcion.obtener_Apel()
            elif select == 3:
                edad = funcion.obtener_edad()
            elif select == 4:
                sexo = funcion.obtener_sexo()
            elif select == 5:
                ciudad = funcion.obtener_ciudad()
            elif select == 6:
                (estatura_cm, estatura_m) = funcion.obtener_estatura()
            elif select == 7:
                amigos = funcion.obtener_lista_amigos()
            elif select == 0:
                actualizar = False
                print()
                print("  Muy bien tus datos quedan así entonces: ")
                funcion.mostrar_perfil(nombre, apellido, sexo, edad, ciudad, estatura_m, estatura_cm, amigos)
                print()

    # Código para la opción 0. Salir.
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ",nombre+".user")
        funcion.escribir_usuario(nombre, apellido, sexo, edad, ciudad, estatura_m, estatura_cm, amigos, estado, muro)
        print("Archivo",nombre+".user","guardado")

print("Gracias por usar Network. ¡Hasta pronto!")
print()
