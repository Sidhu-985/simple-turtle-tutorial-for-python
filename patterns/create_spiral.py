import turtle as t

def create_spiral(turtle, line_length):
    for _ in range(100):
        turtle.forward(line_length)
        turtle.right(30)
        line_length += 1

T = t.Turtle()
create_spiral(T, 5)
