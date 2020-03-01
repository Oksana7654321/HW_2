# Possibility 1:

a=int(input("Enter first number: "))
b=int(input("Enter a second number: "))

a,b=b,a
print("The first number nas been replaced with "+ str(a), "The second number has been replaced with " + str (b))


# Possibility 2:

a=int(input("Enter first number: "))
b=int(input("Enter a second number: "))
a=a+b
b=a-b
a=a-b

print(a,b)