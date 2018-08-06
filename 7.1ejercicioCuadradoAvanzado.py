import turtle

def main():
    window = turtle.Screen()   # abre la ventana para dibujo
    criss = turtle.Turtle()    #nombro mi objeto

    make_square(criss)
    turtle.mainloop()         # evita los que la pantalla se cierre


def make_square(criss):
    length = int(input("What is the size of you square: "))    #pide un dato

    for i in range(4):          #repite la función 4 veces
        make_line_and_turn(criss, length)

def make_line_and_turn(criss, length):
    criss.forward(length)
    criss.left(90)

if __name__ == '__main__':
    main()
