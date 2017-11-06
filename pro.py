import turtle
bob = turtle.Turtle()
from kk import*
turtle.colormode(255)
bob.width(3)
bob.speed(11)
turtle.bgcolor("khaki")

bob.penup()
bob.goto(-100,100)
bob.pendown()
polygon(bob,5,350)
for times in range(37):
  
  bob.color(89-times,0,179-times)
  polygon(bob,3,80)
  bob.color("teal")
  rightcurve(bob)


bob.penup()
bob.goto(220,195)
bob.pendown()
for times in range(37):
  
  bob.color(0,0,179-times)
  polygon(bob,3,80)
  bob.color("red")
  rightcurve(bob)

bob.penup()
bob.right(100)
bob.forward(350)
bob.pendown()
for times in range(37):
  
  bob.color(0,255-times,60)
  polygon(bob,3,80)
  bob.color("yellow")
  rightcurve(bob)

bob.penup()
bob.left(95)
bob.forward(360)
bob.pendown()
for times in range(37):
  
  bob.color(0,56-times,60)
  polygon(bob,3,80)
  bob.color(255,0,226)
  rightcurve(bob)

bob.penup()
bob.right(95)
bob.forward(350)
bob.pendown()
for times in range(37):
  
  bob.color(45,56-times,66)
  polygon(bob,3,80)
  bob.color(25,123,34)
  rightcurve(bob)

bob.penup()
bob.goto(200,-190)
bob.pendown()
for times in range(38):
  
  bob.color(78,92,39)
  polygon(bob,3,80)
  bob.color(25,16,56)
  rightcurve(bob)
