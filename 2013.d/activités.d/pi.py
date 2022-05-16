import math
import random
import sys


i = 1
res0_pi = 0

print("Input")
maxnombre = int(input())

while i<maxnombre:
    x = random.random()
    #print("x",x)
    y = random.random()
    #print("y",y)
    i += 1
    if( x*x + y*y < 1):
        res0_pi += 1

res1_pi = 0
i=0
while i<maxnombre:
    x = random.random()
    #print("x",x)
    y = random.random()
    #print("y",y)
    i += 1
    if( x*x + y*y < 1):
        res1_pi += 1


print("Mon pi",(res0_pi*4/maxnombre + res1_pi*4/maxnombre)/2 ) 





