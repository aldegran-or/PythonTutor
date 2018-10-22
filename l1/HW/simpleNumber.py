#!/usr/bin/python3
#simpleNumber.py
import os
os.system('clear')
n=int(input('введите число:'))
i=2
j=0
while (n>=i*i and j!=1):
    if n%i==0:
        j=1
        i=i+1
    else:
        i=i+1
if j==1:
    print('{0} составное число'.format(n))
else:
    print('{0} простое число'.format(n))
