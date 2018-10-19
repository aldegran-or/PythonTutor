#!/usr/bin/python3
#simpleDigits.py
import os
os.system('clear')
print("программа выводит список простых чисел в указанном диапазоне")
k=int(input('введите первое число:'))
i=int(input('введите второе число:'))
for i in range(k,i+1):
    #print("i=",i)
    for j in range(2,i):
        #print(" j=",j)
        if i%j==0:
            #print("число {0} составное".format(i))
            break
    else:
     print("найдено простое число=",i)
