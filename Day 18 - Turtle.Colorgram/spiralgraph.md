import turtle as t
import random

timmy = t.Turtle()
screen = t.Screen()
timmy.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


for _ in range(100):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 10)

screen.exitonclick()
