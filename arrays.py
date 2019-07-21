from array import *
arr=array('i',[10,25,13,2])

y=len(arr)
for i in arr:
    x = i
    if(i<x):
        temp=x
        x=i
        i=temp
print(arr)