# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:00:08 2024

@author: Диана
"""

from mod import is_deficient_number

n = int(input("Введіть значення n: "))
if is_deficient_number(n):
    print("Число %d є недостатнім числом." % n)
else:
    print("Число %d не є недостатнім числом." % n)