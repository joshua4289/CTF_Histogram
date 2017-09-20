#!/usr/bin/python
import matplotlib.patches as patches
import numpy as np
import math
import matplotlib.pyplot as plt


with open('rlnStigmation.dat','r') as f:
	data = f.read().splitlines()


data = [x.strip() for x in data]
print data
data_float = [float(y) for y in data ]

#split poitive and negative values
data_float_pos = [float(y) for y in data if float(y) > 0]
dat_float_neg = [float(y) for y in data if float(y) < 0 ]


#if x.isintance(x,float)]


#print data_float
#pix_size = 0.89

x_min = int(round(min(data_float),-1))
x_max =int(round(max(data_float),-1))

if x_min > 100: 
	plot_bins = 2500
else:
	plot_bins = 10





#0 to 30 angstroms in incriments of 2 

bins=xrange(x_min,x_max,plot_bins)
plt.hist(data_float, bins=bins)
plt.xticks(xrange(-90,90,30))

#plt.title('Estimated Resolution of Average Images')
txt1= "Total data points =" +str(len(data_float))
txt2="Mean Estimated  =" +str(np.mean(data_float))
txt3="Median Estimated  ="+str(np.median(data_float))
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

        transform=ax.transAxes)





#plt.text(right,top,txt)
plt.show()

