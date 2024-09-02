import turtle as t

def move_turtle(turtle):
    for _ in range(100):
        turtle.forward(50)
        turtle.right(10)

T = t.Turtle()
move_turtle(T)
