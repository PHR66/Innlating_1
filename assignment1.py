"""Innlating 1"""

number = int(input("Skriva eitt heiltal ímillum 10000 og 99999 "))
if number >= 10000 and number < 100000:
	print(number // 10000, '   ', number % 10000 // 1000, '   ', number % 1000 // 100, '   ', number % 100 // 10, '   ', number % 10)
else:
	print("Skriva eitt heiltal ímillum 10000 og 99999 ")