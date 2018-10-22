#!/usr/bin/python3
#simpleNumber.py
import os
os.system('clear')
n=int(input('введите число:'))
i=2
while (n>=i*i and n/i!=1):
    if n%i==0:
        print('{0} составное число'.format(n)) 
        break
    else:
        i=i+1
else:
    print('{0} простое число'.format(n))
