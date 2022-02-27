# **<u>DAY 28 NOTES</u>**

in this lesson, I covered tkinters Canvas Widget
and how this can be used to create Layered GUIs for Users and 
Applications.\
First lesson today intro'd the Canvas tool in Tkinter.
Easily sret with:
    
    myCanvas = Canvas(height=x, width=y, bg=background color(hex value)

Can use _img_file = PhotoImage(file="path\to\file.png")_ 
to set a variable that contains the Image we want to use, so that we can
then use _myCanvas.create_image(xcor, ycor, image=img_file)_ 
to set an image on the canvas. 

Remember to add .pack() to place items

# Dynamic Typing

the ability for variable in python to change their data type 
based on the content of the variable. In todays code, we are able to
switch from int to str while the timer counts down to show
"00" instead of 0