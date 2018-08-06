import turtle

def main():
    window = turtle.Screen()   # abre la ventana para dibujo
    criss = turtle.Turtle()    #nombro mi objeto
    make_square(criss)
    turtle.mainloop()         # evita los que la pantalla se cierre

def make_square(criss):
    length = int(input("Length: "))    #pide un longitud
    side = int(input("Side: "))        # pide dato lados

    if side < 3:
        print("The side must equal or upper 3") #daría angulo llano

    angle = 360/side

    for i in range(side):          #repite la función 4 veces
        criss.forward(length)
        criss.left(angle)       #voltea en el angulo determinado

if __name__ == '__main__':
    main()
