import random 
import sys
import matplotlib.pyplot as plt 


import numpy as np


y = np.array([3,8,1,10])
mylabels = ["A", "B", "C", "D"]

plt.pie(y, labels = mylabels)
plt.show()