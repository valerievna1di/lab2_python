# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:48:35 2024

@author: Диана
"""

import math

def z_calc (x):
    if x == 0:
        x = int(input("Введіть значення х ще раз: "))
    z = math.sqrt(2) / 2 * math.sin(1 / x) + 1
    return z
def is_deficient_number(n):
    sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors < n

x = int(input("Введіть значення x, яке не рівне нулю: "))
print("Значення виразу z = ", z_calc(x))

n = int(input("Введіть значення n: "))
if is_deficient_number(n):
    print("Число %d є недостатнім числом." % n)
else:
    print("Число %d не є недостатнім числом." % n)