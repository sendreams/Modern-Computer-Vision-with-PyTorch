import numpy as np

a = np.random.rand(1, 2)
b = np.random.rand(2, 3)
c = np.dot(a, b)
print("a:\n", c)
d = a @ b
print("b:\n", d)
