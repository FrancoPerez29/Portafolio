import turtle
turtle.title("Flower")
turtle.bgcolor("black")
turtle.speed(0)



for i in range(20):
    for colores in ("red","blue","green","purple","yellow","grey","orange","white","pink" ):
        turtle.color(colores)
        turtle.circle(200 -i*9 ,90)
        turtle.lt(90)
        turtle.circle(200 -i*9 ,90)
        turtle.lt(90)
        turtle.left(45)
    

turtle.done()