import numpy
from matplotlib import pyplot as mat

x=numpy.linspace(-numpy.pi * 2, numpy.pi * 2, 720)
cos, sin=numpy.cos(x), numpy.sin(x)
mat.plot(x, sin, ls=':', label='sin')
mat.plot(x, cos, ls='--', label='cos')
mat.title("Graph of sin cos")
mat.xlabel('radians')
mat.ylabel('value')
mat.grid()
mat.legend()
mat.show()
