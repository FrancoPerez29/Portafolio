import turtle

t = turtle.Screen()
t.title("diseño en turtle")
t.bgcolor("white")


s = turtle.shapesize()
# Drawing circles of different colors and sizes.
for i in range(400):
    for colores in ("red","blue","green","purple","yellow","grey","orange","black"):
        turtle.color(colores)
        turtle.speed(20)
        turtle.circle(i)
        turtle.circle(i*2)
        turtle.right(5)
        turtle.forward(5)
        
        
        
        
turtle.done()