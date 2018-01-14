from turtle import *

screen = Screen()
screen.setup(400, 400)

colours = { 
  'miu miu': '#E08484',
  'kitty': '#6599CC',
  'tree': '#65CC99'
}

print(colours['miu miu'])
print(colours['kitty'])
print(colours['tree'])

screen.bgcolor(colours['miu miu'])


circle(50)
dot(100)

penup()
color(colours['kitty'])
style = ('Arial', 60, 'bold')
write('HELLO', font=style, align='center')

right(90)
forward(70)
color(colours['tree'])
write('WORLD!', font=style, align='center')
hideturtle()