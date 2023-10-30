"""Exercise 2.12"""
# Formula a = p(1 + r) ** n

p = 1000.0
r = 0.07
n = 10

a = p * r**n

print(a)

n = n * 2
a = p * r**n

print(a)

n = n * 3
a = p * r**n

print(a)