import sys, platform
import numpy as np

print("=== Runtime Info ===")
print("Python:", sys.version.split()[0])
print("Platform:", platform.node())

print("\n=== Numpy Test ===")
a = np.arange(9).reshape(3,3)
b = np.ones((3,3))
print("a:\n", a)
print("b:\n", b)
print("a @ b:\n", a @ b)