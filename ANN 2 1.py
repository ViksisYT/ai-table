import numpy as np

x = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

w = np.array([[1],
              [1]])

s = np.dot(x,w)

print(s)
print("bye! the script ends.")
