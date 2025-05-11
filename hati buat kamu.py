from turtle import *
import math

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)
bgcolor("black")
color("red")
hideturtle()

for i in range(0, 360, 2):
    k = math.radians(i)
    x = hearta(k) * 10
    y = heartb(k) * 10
    penup()
    goto(0, 0)
    pendown()
    goto(x, y)

done()