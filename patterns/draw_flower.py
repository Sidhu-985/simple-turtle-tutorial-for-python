import turtle as t
T = t.Turtle()

def draw_flower(turtle, petals, radius):
    for _ in range(petals):
        turtle.circle(radius)
        turtle.left(360 / petals)



T.speed(0)  
draw_flower(T, petals=12, radius=100)
