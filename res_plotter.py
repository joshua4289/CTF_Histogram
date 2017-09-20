#!/usr/bin/python
import matplotlib.patches as patches
import numpy as np
import math
import matplotlib.pyplot as plt


with open('rlnRes.dat','r') as f:
	data = f.read().splitlines()


data = [x.strip() for x in data]
data_float = [float(y) for y in data]


#0 to 30 angstroms in incriments of 2 

bins=np.arange(0,10,0.25)
plt.hist(data_float, bins=bins)
plt.xticks(np.arange(0,10,0.5))
plt.title('Estimated Resolution of Average Images',fontsize=22)
txt1= "Total data points =" +str(len(data_float))
txt2="Mean Estimated Resolution =" +str(np.mean(data_float))
txt3="Median Estimated Resolution ="+str(np.median(data_float))
txt= str(txt1)+ '\n' +str(txt2)+'\n'+str(txt3)
#making space for text annotate
left, width = .4, .5

bottom, height = .25, .5

right = left + width

top = bottom + height

ax = plt.gca()

p = patches.Rectangle(

    (left, bottom), width, height,

    fill=False, transform=ax.transAxes, clip_on=False

    )

ax.text(right, top, txt,

        horizontalalignment='right',

        verticalalignment='top',

        transform=ax.transAxes,
        fontsize=18)





#plt.text(right,top,txt)
plt.show()

