# Week 1.5, Session 2: Task 3
from money import Money
# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum
m1 = Money(1,99)
m2 = Money(0,50)
total=m1.__add__(m2)
print(total.__str__())