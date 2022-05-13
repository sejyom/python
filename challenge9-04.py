import turtle as t

t.speed(0)
for i in range(60):
    for j in range(5):
        t.forward(100)
        t.left(360/5)
    t.left(360//60)
