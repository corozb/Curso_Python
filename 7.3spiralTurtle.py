import turtle

window = turtle.Screen() #abre la pantalla blanca de dibujo

colors=['red','purple','blue','green','yellow','orange']

t = turtle.Pen() #pen quiere decir lapicero de dibujo
t.speed(0)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

turtle.mainloop()   #permite que termine
