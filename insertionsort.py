# import all the modules 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 
import matplotlib as mp 
import numpy as np 
import random 
  
# set the style of the graph 
plt.style.use('fivethirtyeight') 
  
# input the size of the array (list here) 
# and shuffle the elements to create 
# a random list 
n = int(input("Enter array size: \n")) 
a = [i for i in range(1, n+1)] 
random.shuffle(a) 
  
# insertion sort 
def insertionsort(a): 
    for j in range(1, len(a)): 
        key = a[j] 
        i = j-1
  
        while(i >= 0 and a[i] > key): 
            a[i+1] = a[i] 
            i -= 1
  
            # yield the current position 
            # of elements in a 
            yield a 
        a[i+1] = key 
        yield a 
  
  
# generator object returned by the function 
generator = insertionsort(a) 
  
# to set the colors of the bars. 
data_normalizer = mp.colors.Normalize() 
color_map = mp.colors.LinearSegmentedColormap( 
    "my_map", 
    { 
        "red": [(0, 1.0, 1.0), 
                (1.0, .5, .5)], 
        "green": [(0, 0.5, 0.5), 
                  (1.0, 0, 0)], 
        "blue": [(0, 0.50, 0.5), 
                 (1.0, 0, 0)] 
    } 
) 
  
  
fig, ax = plt.subplots() 
  
# the bar container 
rects = ax.bar(range(len(a)), a, align="edge", 
               color=color_map(data_normalizer(range(n)))) 
  
# setting the view limit of x and y axes 
ax.set_xlim(0, len(a)) 
ax.set_ylim(0, int(1.1*len(a))) 
  
# the text to be shown on the upper left 
# indicating the number of iterations 
# transform indicates the position with 
# relevance to the axes coordinates. 
text = ax.text(0.01, 0.95, "", transform=ax.transAxes) 
iteration = [0] 
  
# function to be called repeatedly to animate 
  
  
def animate(A, rects, iteration): 
  
    # setting the size of each bar equal 
    # to the value of the elements 
    for rect, val in zip(rects, A): 
        rect.set_height(val) 
  
    iteration[0] += 1
    text.set_text("iterations : {}".format(iteration[0])) 
  
  
anim = FuncAnimation(fig, func=animate, 
                     fargs=(rects, iteration), frames=generator, interval=50, 
                     repeat=False) 
  
plt.show() 