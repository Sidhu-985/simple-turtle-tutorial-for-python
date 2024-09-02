import turtle as t

T = t.Turtle()

def bounce_ball(turtle_obj):
    while True:
        turtle_obj.forward(10)
        if turtle_obj.xcor() > 200 or turtle_obj.xcor() < -200:
            turtle_obj.right(180)
        if turtle_obj.ycor() > 200 or turtle_obj.ycor() < -200:
            turtle_obj.right(180)

bounce_ball(T)
