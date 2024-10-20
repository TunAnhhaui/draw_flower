import turtle
import colorsys

turtle.speed(0)
#turtle.tracer(0)

turtle.bgcolor("black")

NUMBER_OF_PETHALS = 16
NUMBER_OF_PENTAL_VEINS = 18

hue = 0

for i in range(NUMBER_OF_PETHALS):
    
    for j in range(NUMBER_OF_PENTAL_VEINS):
        
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        
        turtle.color(color)
        
        hue += 0.005
        
        turtle.right(90)
        radius = 150 - j * 6
        turtle.circle(radius, 90)
        
        turtle.left(90)
        turtle.circle(150 - j * 6, 90)
        
        turtle.right(180)

    turtle.circle(40, 24)

text = "Chúc chị ngày 20/10 vạn sự như ý 8386 <3"

font_size = 14 
character_spacing = 15  
text_width = len(text) * character_spacing 

screen_width = 400 
start_x = -text_width / 2 

turtle.penup()
turtle.goto(start_x, -250) 
turtle.setheading(0) 
turtle.pendown()

hue = 0

for char in text:
    color = colorsys.hsv_to_rgb(hue, 1, 1) 
    turtle.color(color) 
    turtle.write(char, font=("Arial", font_size, "bold"))
    hue += 0.05  
    turtle.forward(character_spacing) 

turtle.update()
turtle.done()
