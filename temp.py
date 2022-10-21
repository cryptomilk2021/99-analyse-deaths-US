import numpy as np
import matplotlib.pyplot as plt

top=[('2017-12-05',1.875),('2017-12-05',1.125),('2017-12-05',0.5)]

labels, ys = zip(*top)
xs = np.arange(len(labels))
width = 1

fig = plt.figure()
ax = fig.gca()  #get current axes
ax.bar(xs, ys, width, align='center')

#Remove the default x-axis tick numbers and
#use tick numbers of your own choosing:
ax.set_xticks(xs)
#Replace the tick numbers with strings:
ax.set_xticklabels(labels)
#Remove the default y-axis tick numbers and
#use tick numbers of your own choosing:
ax.set_yticks(ys)


plt.show()
