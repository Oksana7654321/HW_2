inp = list(input('Please enter any four-digit natural number: '))

print ("1. Multiply the digits")

product = 1;
for i in inp:
	product *= int(i)
print(product)

print("2. Reverse the digits")
inp.reverse()
print(inp)

print ("3. Order the digits")
inp.sort()
print(inp)