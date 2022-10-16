import random 
import sys
import matplotlib.pyplot as plt 


import numpy as np

xpoints = np.array(["A","B","C","D"])
ypoints = np.array([5,10,15,20])

plt.xlabel("Character")
plt.ylabel("Number")
plt.bar(xpoints, ypoints)
plt.show()