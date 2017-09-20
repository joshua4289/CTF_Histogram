#!/usr/bin/python
import matplotlib.patches as patches
import numpy as np
import math
import matplotlib.pyplot as plt


with open('rlnDefocusU.dat','r') as f:
	data = f.read().splitlines()


data = [x.strip() for x in data]
data_float = [float(y) for y in data if float(y) >= 0]



x_min = int(round(min(data_float),-1))
x_max =int(round(max(data_float),-1))

if x_min > 100: 
	plot_bins = 500






bins=xrange(x_min,x_max,500)
plt.hist(data_float, bins=bins)

#variable controls only xticks
x_ticks_per = 10000
plt.xticks(xrange(0,((x_max/x_ticks_per) *x_ticks_per),x_ticks_per))

#plt.title('Estimated Resolution of Average Images')

#remove during final plot 

#txt1= "Total data points =" +str(len(data_float))
#txt2="Mean Estimated  =" +str(np.mean(data_float))
#txt3="Median Estimated  ="+str(np.median(data_float))
#txt= str(txt1)+ '\n' +str(txt2)+'\n'+str(txt3)
#making space for text annotate
#left, width = .25, .5

#bottom, height = .25, .5

#right = left + width

#top = bottom + height

#ax = plt.gca()

#p = patches.Rectangle(

#    (left, bottom), width, height,

#    fill=False, transform=ax.transAxes, clip_on=False

#    )

#ax.text(right, top, txt,

#        horizontalalignment='right',

#        verticalalignment='top',

#        transform=ax.transAxes)





#plt.text(right,top,txt)
plt.show()

