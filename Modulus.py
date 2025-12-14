# a = 12 
# b = 13
# print(b%a)

# a = int(input("enter number:1 "))
# b = int(input("enter number:2 "))
# remainder = b%a
# print(remainder)

a = int(input("enter number 1: "))
b = int(input("enter number 2: "))

if a != 0:
    remainder = b % a
    print(remainder)
else:
    print("Division by zero not allowed")
