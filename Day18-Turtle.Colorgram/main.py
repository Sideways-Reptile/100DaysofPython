# CODE USE TO EXTRACT COLOR PALETTE FROM CHOSEN IMAGE FILE
# # import colorgram     -this tool is used to get color info
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

# Hirtsch Painting Challenge

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
color_list = [(244, 234, 216), (215, 156, 85), (116, 169, 205), (211, 228, 240), (60, 100, 144), (174, 85, 46),
              (152, 55, 94), (243, 226, 236), (145, 15, 42), (229, 244, 237), (168, 165, 38), (56, 122, 82),
              (68, 16, 34), (44, 27, 18), (220, 204, 113), (214, 87, 58), (27, 31, 59), (132, 178, 153),
              (191, 141, 170), (26, 47, 36), (178, 95, 137), (97, 116, 181), (34, 50, 119), (65, 153, 179),
              (147, 27, 17), (223, 173, 200), (32, 83, 60), (153, 208, 221), (91, 154, 110), (232, 176, 160)]
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
