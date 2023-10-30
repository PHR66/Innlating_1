"""Exercise 2.12"""
# Formula a = p(1 + r) ** n where p is start amount, r is interrest rate and n periode

p = 1000.00
r = 0.07
n = 10

a = p * (1 + r)**n

print(a)

n = n * 2
a = p * (1 + r)**n

print(a)

n = n * 3
a = p * (1 + r)**n

print(a)