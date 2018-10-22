#!/usr/bin/python3
#simpleNumber.py
import os
os.system('clear')
n = int(input("n="))
lst=[]
for i in range(2, n+1):
    # пробегаем по списку (lst) простых чисел
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)
print(lst)
