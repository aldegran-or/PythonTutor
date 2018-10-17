#!/usr/bin/python3
#addition_subtraction.py
import os
os.system('clear')
print("сложение или вычитание чисел 'a' и 'b'")
print("----------------------------------------------------")
print("Введите числа:\n")
a=float(input('a:'))
b=float(input('b:'))
#print('выбор сложение (+) или вычитание (-) :'.rstrip('\n')),
sign=input('выбор сложение (+) или вычитание (-) : ')
if sign == "+":
    print('сумма чисел {0} и {1} равна '.format(a, b), a+b)
elif sign == "-":
    print('разница чисел {0} и {1} равна '.format(a, b), a-b)
else:
    print('значение Знака неверно!')
