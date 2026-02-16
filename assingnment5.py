# create a function with no parameters that calculates the area of a rectangle
def area():
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    area = length * width
    print("The area of the rectangle is:", area)

area()

print('=================================')
def addition():
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    sum = a + b
    print("The sum is ", sum)

addition()

print('================================')
def subtraction():
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    difference = a - b
    print("The differnce is ", difference)

subtraction()

print('===================================')
def division(a, b):
    a = 10
    b = 2
    quotient = a / b

    print("The quotient is: ", quotient)
division()
    
def check_number():
    num = int(input("Enter a number"))
    if num >0:
        print("Number positive")
    elif num < 0:
        print("Number negative")
    else:
        print("Number is zero")

check_number()