# Um simples teste da biblioteca matplotlib

import matplotlib
import matplotlib.pyplot as plt
import math


x_axis = range(0, 2000)
x_axis = [x / 100 for x in x_axis]
y_axis = [math.sin(x) for x in x_axis]

fig, ax = plt.subplots()
ax.plot(x_axis, y_axis)
ax.set(xlabel='x (radians)', ylabel='sin(x)', title='How Sine Wave Looks Like')
ax.grid()

fig.savefig("Test.png")
plt.show()
