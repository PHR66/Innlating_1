
"""Exercise 2.11"""

number = int(input("Skriva eitt heiltal ímillum 10000 og 99999 "))
if number >= 10000 and number < 100000:
	print(number // 10000, '   ', number % 10000 // 1000, '   ', number % 1000 // 100, '   ', number % 100 // 10, '   ', number % 10)
else:
	print("Skriva eitt heiltal ímillum 10000 og 99999 ")


"""Exercise 2.12"""
# Formula a = p(1 + r)**n

p = 1000.0
r = 1.07
n = 10

a = p * r**n

print(a)

n = n * 2
a = p * r**n

print(a)

n = n * 3
a = p * r**n

print(a)