#!/usr/bin/python3
#simpleDigits.py
import os
os.system('clear')

div=0
i=int(input('i:'))
for i in range(2,i+1):
    #print("i=",i)
    for j in range(2,i):
        #main=i/j
        last=i%j
        if last==0:
            div=div+1
        #print("i={0} : j={1} last={2} div={3}".format(i, j, last, div))
    if div==0:
        print("simpleNumber=",i)
    else:
        div=0
