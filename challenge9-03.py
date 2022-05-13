import turtle as t

t.setup(500, 500)
t.bgcolor('black')
color=['yellow', 'red', 'blue']

t.speed(0)
# t.pensize(i/200)+1
for i in range(200):
    t.pencolor(color[i%len(color)]) #i%len(color)
    t.width(i/200+1)
    t.forward(i*2)
    t.left(119)
