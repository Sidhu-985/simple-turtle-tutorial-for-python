import turtle as t

T = t.Turtle()

def draw_square(turtle, size):
  
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

draw_square(T, 100)
