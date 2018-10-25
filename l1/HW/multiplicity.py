#!/usr/bin/python3
#multiplicity.py
import os
os.system('clear')
lst=[]
print('программа выводит все числа из определённого диапазона кратные заданному')
n = int(input("Начало диапазона="))
k = int(input("Конец диапазона="))
f = int(input("Кратность="))
for i in range(n, k+1):
    if i%f==0:
        lst.append(i)
#print(lst)        
for j in range(len(lst)):
    print(lst[j], end =" ")
print()

