# Sanu K Joseph
from statistics import mean  
from math import pi 
from time import time,ctime

seconds = time()

print("The value of pi is", pi) 
print("Epoch Time =", seconds) 
print("Local time:", ctime(seconds))
print("The average of list values is : ", end="") 
print(mean([1, 2, 3, 3, 2, 2, 2] )) 
