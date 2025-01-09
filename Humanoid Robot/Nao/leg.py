import csv
from pickle import APPEND
import matplotlib.pyplot as plt

teta0 = []
teta1 = []
teta2 = []
teta3 = []
teta4 = []
teta5 = []


with open("leg.txt", "r") as f:

    f = open("leg.txt", "r")
    for i in f:
        a0,a1,a2,a3,a4,a5 = i.split()
        teta0.append(float(a0))
        teta1.append(float(a1))
        teta2.append(float(a2))
        teta3.append(float(a3))
        teta4.append(float(a4))
        teta5.append(float(a5))

f.close()

fig = plt.figure()

plt.subplot(2, 2, 1)
plt.plot(teta0)

plt.subplot(2, 2, 2)
plt.plot(teta1)

plt.subplot(2, 2, 3)
plt.plot(teta2)

plt.subplot(2, 2, 4)
plt.plot(teta3)

plt.show()
