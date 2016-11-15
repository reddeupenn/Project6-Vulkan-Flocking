#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

'''
num particles  x1024  : 1    2     4     8   12  16   20     
AABB optimisation off : 1    3.5   10.5  39  84  148  232
AABB optimisation on  : 1.2  3.8   12    44  96 230  264   
'''


N = 7
defaultMeans = (1, 3.5, 10.5, 39, 84, 148, 232)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, defaultMeans, width, color='#cc1111')

scissorMeans = ( 1.2, 3.8, 12, 44, 96, 230, 264)
rects2 = ax.bar(ind + width, scissorMeans, width, color='#0088cc')

# add some text for labels, title and axes ticks
ax.set_ylabel('time (ms)')
ax.set_title('simulation time')
ax.set_xticks(ind + width)
ax.set_xticklabels(('1x1024', '2x1024', '4x1024', '8x1024', '12x1024', '16x1024', '20x1024'))

ax.legend((rects1[0], rects2[0]), ('AABB test off', 'AABB test on'), loc=2)
ax.axis((0,7,0,290))


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                '%.1f' % float(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
