#!/bin/python3
from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
   write(step, align='center')
   right(90)
   forward(10)
   pendown()
   forward(150)
   penup()
   backward(160)
   left(90)
   forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100) #x and y like a graph
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 80)
bob.pendown()

miu = Turtle()
miu.color('green')
miu.shape('turtle')

miu.penup()
miu.goto(-160, 60)
miu.pendown()

patty = Turtle()
patty.color('pink')
patty.shape('turtle')

patty.penup()
patty.goto(-160, 40)
patty.pendown()

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  miu.forward(randint(1,5))
  patty.forward(randint(1,5))

