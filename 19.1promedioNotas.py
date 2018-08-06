def listaNotas(totalNotas):
    totalNotas=int(input('Cuantas notas son en total '))
    for i in range(0,totalNotas):
        dato=float(input('Ingresa tus notas(una a la vez): '))
        notas.append(dato)
    return totalNotas

def promedio():
    totalNotas = listaNotas(notas)
    sumPromedio=0
    for promedio in notas:
        sumPromedio+= float(promedio)
        notaFinal = sumPromedio /totalNotas
    print(notas)
    print('su promedio es {0:.2f}'.format(notaFinal))

    if notaFinal <= 3.0:
        print(" ")

        print('Creo que mejor le rezas a la Rosa de Guadalupe a ver si te hace el milagrito y puedes regresar a casa')
    else:
        print(" ")
        print('Tranqui esta vez te acompaño la suerte. SACUDETE y ve tranquilo a casa. Aún eres bienvenido.  ')



if __name__=='__main__':
    notas = []
    print(" ")
    print(" ")
    print('Chico no fuiste muy aplicado este semestre. LO SE. Por eso estás aquí calculando tu promedio y ya sea para estar tranquilo y darle la buena noticia a tus padres o por el contrario comprar un ticket a un país donde nadie te encuentre')
    print(" ")
    print('Bueno no más angustias y empezemos....')
    promedio()
