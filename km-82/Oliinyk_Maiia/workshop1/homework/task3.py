""""
Обчислити суму( i:((x^2+1)^(0,5))) . I від 1 до n
"""

def task3():
"""
Обчислює суму дробів
Args:викликаються в самій функції
Return: одне дійсне число
"""

x = float(input("\nУведіть значення x:   "))
n = int(input("\nУведіть значення n(ціле додатнє число):   "))

import math

rez = 0

  for i in range(1, n + 1):
    rez += i / (math.sqrt((x ** 2) + 1))

return(print(rez))