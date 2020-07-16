#!python3

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

file_name = "./loss.txt"
with open(file_name) as f:
    data = f.read()
f.close()

lines = data.splitlines()

x = []
loss = []
average = []

for line in lines:
    d_l = line.split(" ")
    x.append(int(d_l[0]))
    loss.append(float(d_l[2]))
    average.append(float(d_l[5]))

fig, ax = plt.subplots(1, 1, figsize=(10,10), facecolor='#cccccc')

ax.set_facecolor('#eafff5')
ax.set_title('My Pretty Graph by La Labomedia', size=32, color='magenta')

ax.set_ylim(0, 12)

ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)

ax.set_xlabel('Steps (number)', color='coral', size=20)
ax.set_ylabel('Loss', color='coral', size=20)

l = ax.plot(x, loss,
            linestyle=(0, (3, 5, 1, 5)),
            linewidth=1.5,
            color='red',
            label="Loss")

a = ax.plot(x, average,
            linestyle=(0, (5, 5)),
            linewidth=1.5,
            color='green',
            label="Average")

ax.axhline(y=0.1, xmin=0.0, xmax=1, color='r')

ax.text(200000, 0.2, "Objectif = 0.1", weight='bold', color='blue')

ax.legend(loc="upper right", title="Efficiency")

fig.savefig("loss.png")
plt.show()



# #ax.xaxis.set_major_locator(MultipleLocator(20))
# #ax.xaxis.set_minor_locator(AutoMinorLocator(5))
# #ax.yaxis.set_major_locator(MultipleLocator(20))
# #ax.yaxis.set_minor_locator(AutoMinorLocator(5))
# #ax.tick_params(which='major', width=1.0)
# #ax.tick_params(which='major', length=10)
# #ax.tick_params(which='minor', width=1.0, labelsize=10)
# #ax.tick_params(which='minor', length=5, labelsize=10, labelcolor='0.25')
