from scipy import io
import numpy as np

# ---------------------- exporting data in matlab format --------------------- #

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

io.savemat('arr.mat', {"vec": arr})

# ---------------------- importing data from matlab format --------------------- #

mydata = io.loadmat('arr.mat', squeeze_me=True)

print(mydata)
print(mydata['vec'])
