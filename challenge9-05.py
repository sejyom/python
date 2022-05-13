from turtle import *
from random import *

setup(800, 500)
tshs=['arrow', 'circle', 'turtle', 'square', 'triangle', 'classic']
han=['화살', '원', '거북이', '사각형', '삼각형', '전통']
cols=['red', 'blue', 'green', 'purple', 'magenta', 'black', 'gray',
      'yellow', 'cyan', 'orange', 'aqua']
boolean=True
speed(0)
for i in range(20):
    r=randint(0, len(tshs)-1)
    p=randint(0, len(cols)-1)
    penup()
    radius=randint(3,50)
    x=randint(-300, 300)
    y=randint(-200, 200)
    goto(x, y)
    
    pendown()
    shape(tshs[r])
    fillcolor(cols[p])
    begin_fill()
    circle(radius)
    end_fill()
    pensize(1)
    pencolor(cols[randint(0, len(cols)-1)])
    write(han[r])
