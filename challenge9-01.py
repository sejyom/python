from random import random
import math

radius=round(random(), 3)*10


def getarea(r):
    return r*r*math.pi


print('원의 반지름: %.2f' % radius)
print('원주율 pi: %.2f' % math.pi)
print('반지름 %2.f인 원의 면적은 %.2f' % (radius, getarea(radius)))
