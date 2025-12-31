import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3.14, 100)
y = np.sin(x) + 1.5

area = np.trapezoid(y, x)

plt.fill_between(x, y)
plt.title(f'Area = {area:.2f}')
plt.show()