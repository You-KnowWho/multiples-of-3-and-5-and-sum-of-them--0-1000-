# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 17:10:47 2017

@author: Narukurti Kavya
"""

#multiples of 3 and 5

i=0
num=[]
for i in range (0,1000):
    if i%3==0:
        num.append(i)
        i=i+1
    elif i%5==0:
        num.append(i)
        i=i+1
    else:
        i=i+1
         
print num

print len(num)

sum=0
j=0

for j in range (len(num)):
    sum += num[j]
     
print sum

    

    
    
        