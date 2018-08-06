#El módulo 'os' nos permitirá consultar si un archivo existe.
import os

def bienvenida():
    print("Bienvenido a ... ")
    print("""
     _   _      ___          __        _    
    | \ | |    | \ \        / /       | |   
    |  \| | ___| |\ \  /\  / /__  _ __| | __
    | . ` |/ _ \ __\ \/  \/ / _ \| '__| |/ /
    | |\  |  __/ |_ \  /\  / (_) | |  |   < 
    |_| \_|\___|\__| \/  \/ \___/|_|  |_|\_\
    """)
    #fuente para el texto http://www.network-science.de/ascii/
    print()

def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas. ")
    return nombre

def obtener_Apel():
    apellido = input("Para preparar tu perfil dame más información, cuál es tu apellido? ")
    return apellido

def obtener_sexo():
    sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    while sexo != 'M' and sexo != 'F':
        sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    return sexo

def obtener_edad():
    fecha = int(input("Cuál es tu año de nacimiento?. "))
    return 2018-fecha-1

def obtener_ciudad():
    ciudad = input("En que ciudad vives?: ")
    return ciudad

def obtener_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    return (estatura_cm, estatura_m)

def obtener_lista_amigos():
      #amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))
    linea = input("Muy bien. Finalmente, escribe una lista con los nombres de tus amigos, separados por una ',': ")
        # se le ooloca split para que haga una lista con los elemetos separados por split
    amigos= linea.split(",")
    print(linea)
#    nuev_nombre = input("como se llama el nuevo ")
#    linea.append(nuev_nombre)
#    print(linea)
    return amigos

def obtener_datos():
    n = obtener_nombre()
    a = obtener_Apel()
    s = obtener_sexo()
    e = obtener_edad()
    m = obtener_ciudad()
    (em, ec) = obtener_estatura()
    na = len(obtener_lista_amigos())
    return (n,a,s,e,m,em,ec,na)

#Con este código resumimos el proceso de impresión
def mostrar_perfil(nombre, apellido, sexo, edad, ciudad, estatura_m, estatura_cm, amigos):
    print("--------------------------------------------------")
    print("Nombre: ", nombre, apellido)
    print("Género: ", sexo)
    print("Edad:   ", edad, "años")
    print("Ciudad: ", ciudad)
    print("Mides:  ", estatura_m, "metro con", estatura_cm, "centimetros")
    # se le agrega len para que me cuente los nombre de los amigos
    print("Tienes  ", len(amigos), "amigos")
    print("--------------------------------------------------")

def opcionMenu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Mostar mi muro")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion < 0 or opcion > 4:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")
        opcion = int(input("Ingresa una opción: "))
    return opcion

def pubMensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    return mensaje

#esta era la funcion para enviar mensaje a cada uno de mis amigos:
#def mostrar_mensaje(origen, destinatario, mensaje):
#    print("--------------------------------------------------")
#    if destinatario == None:
#        print(origen, "dice:", mensaje)
#    else:
#        print(origen, "dice:", "@"+destinatario, mensaje)
#    print("--------------------------------------------------")

#Ahora como lo que queremos es publicar en un muro con mis amigos se maneja así:
def mostrar_mensaje(origen, mensaje):
    print("--------------------------------------------------")
    print(origen+" dice:"+ mensaje)
    print("--------------------------------------------------")

#Muestra los mensajes recibidos:
def mostrar_muro(muro):
    print("------ MURO ("+str(len(muro))+", mensajes)--------" )
    for mensaje in muro:
        print(mensaje)
    print("--------------------------------------------------")

#Publica un mensaje en el timeline personal y en el de los amigos
def publicar_mensaje(origen, amigos, mensaje, muro):
    print("--------------------------------------------------")
    print(origen, "dice: ", mensaje)
    print("--------------------------------------------------")

    # Agrega el mensaje al final del timeline local. Append agrega elementos a una lista
    muro.append(mensaje)

    # Agrega, al final del archivo de cada amigo, el mensaje publicado
    for amigo in amigos:
        if existe_archivo(amigo+".user"):
            archivo = open(amigo+".user", "a")
            archivo.write(origen+":"+mensaje+"\n")
            archivo.close

def actualizar_datos():
    print()
    print("Que dato deseas actualizar?: ")
    print("  1. Nombre      5. Ciudad")
    print("  2. Apellido.   6. Estatura")
    print("  3. Edad        7. Amigos")
    print("  4. Sexo        0. Actualizar")
    select = int(input(" Selecciona una opción: "))

    while select < 0 or select > 7:
        print("Esa opción no es valida, MIRE BIEN 0 A 7")
        select = int(input("Selecciona una opción: "))
    return select
    print()

def existe_archivo(ruta):
    return os.path.isfile(ruta)

#Observa también como se han modificado las funciones leer_archivo() y escribir_archivo()
#para ser concordantes con la nueva estructura de los archivos ".user"
def leer_usuario(nombre):
    archivo_usuario = open(nombre+".user","r")
    nombre = archivo_usuario.readline().rstrip()
    apellido = archivo_usuario.readline().rstrip()
    sexo = archivo_usuario.readline().rstrip()
    edad = int(archivo_usuario.readline())
    ciudad = archivo_usuario.readline().rstrip()
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    amigos = archivo_usuario.readline().rstrip().split(",")
    estado = archivo_usuario.readline().rstrip()
    # Lee el 'muro'. Esto es, todos los mensajes que han sido publicados en el timeline del usuario.
    muro = []
    mensaje = archivo_usuario.readline().rstrip()
    while mensaje !="":
        muro.append(mensaje)
        mensaje =archivo_usuario.readline().rstrip()

    #Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()
    return(nombre, apellido, sexo, edad, ciudad, estatura_m, estatura_cm, amigos, estado, muro)

def escribir_usuario(nombre, apellido, sexo, edad, ciudad, estatura_m, estatura_cm, amigos, estado, muro):
    archivo_usuario = open(nombre+".user","w")
    archivo_usuario.write(nombre+"\n")
    archivo_usuario.write(apellido+"\n")
    archivo_usuario.write(sexo+"\n")
    archivo_usuario.write(str(edad)+"\n")
    archivo_usuario.write(ciudad+"\n")
    archivo_usuario.write(str(estatura_m + estatura_cm/100)+"\n")
    #archivo_usuario.write(str(num_amigos)+"\n") se cambia valor:
    archivo_usuario.write(",".join(amigos)+"\n")
    archivo_usuario.write(estado+"\n")
    # Escribe el 'timeline' en el archivo, a continuación del último estado
    for mensaje in muro:
        archivo_usuario.write(mensaje+"\n")
    #Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
    archivo_usuario.close()
