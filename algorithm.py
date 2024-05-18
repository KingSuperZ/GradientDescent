"""This code takes any point on a graph and progessively tries to reach the nearest local minimum

This is called Gradient Descent
"""

import matplotlib.pyplot as plt
import numpy as np

# Equation: x^3-5x    Derivative/Slope: 3x^2-5
# Does the entire algorithm for gradient descent
x = 3 # initial guess for the value of x
lr = 0.01
xlist = [x]
for i in range(30):
    x = x-lr*(3*(x**2)-5)
    xlist.append(x)
#print(x)
#plt.plot(xlist)

# Graphs the overall curve
xcurve = np.arange(-3,3,0.001)
ycurve = xcurve**3-5*xcurve
plt.plot(xcurve,ycurve)
plt.axis("equal")
# Plots the points being used in the path for gradient descent
xdescent = np.array(xlist)
ydescent = xdescent**3-5*xdescent
plt.scatter(xdescent,ydescent,s = 20)
