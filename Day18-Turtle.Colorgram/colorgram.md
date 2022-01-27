import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")
print(timmy)


# timmy.shape("turtle")
# timmy.color("DarkTurquoise")
# DRAW A SQUARE; W DOTTED LINES
# for _ in range(4):
#     for _ in range(15):
#         timmy.forward(10)
#         timmy.penup()
#         timmy.forward(10)
#         timmy.pendown()
#     # timmy.forward(100)
#     # timmy.right(90)
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# DRAW SHAPES FROM 3 TO 10 SIDES
# colors = ["CornFlowerBlue", "DarkOrchid", "SlateGrey",
#           "SeaGreen", "wheat", "DarkTurquoise",
#           "IndianRed", "DeepSkyBlue", "LightSeaGreen"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


#
# directions = [0, 90, 180, 270]


# Random Walk image
# timmy.width(15)
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))


# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shapes(shape_side)

# Spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 10)


draw_spirograph(5)

my_screen = t.Screen()
my_screen.exitonclick()
