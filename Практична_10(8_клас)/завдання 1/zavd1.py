# -*- coding: utf-8 -*-
from math import pi, sin, cos # імпортуємо необхідні бібліотеки, для роботи

# створюємо перемінні, і значення

length = int(input("Введіть довжину гірки : "))

angle = int(input("Введіть кут нахилу гірки : "))

radian = angle * pi/180 # формула для вирахування радіанів

a = length * sin(radian) # вираховуємо висоту гірки

b = length * cos(radian) # вираховуємо довжину основи

# виводимо результат на екран

print(round(a))
print(round(b))