import turtle
turtle.Screen()
rainbow=turtle.Turtle()

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
while True:
    for i in range(200):
        rainbow.pencolor(colors[i%len(colors)])
        rainbow.width(i/100+1)
        rainbow.forward(i)
        rainbow.left(59)
turtle.done()