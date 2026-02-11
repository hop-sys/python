# Python functions
# They are a block of code/statement that performs a given task/action
# They can be re-used throughout the program to perform different tasks.
# Functions are defined using the def keyword. (define)
# We have two main types of functions i.e:
# 1. In-built functions -> They come preinstalled with the interpretor i.e print(, pop(), range(), append() etc...
# 2. User defined functions -> They are created by a programmer to solve a given task.
# To define a function you need to give it a name followed by paranthesis.
# For the function body it usually indented and to invoke a function we use the function name.


def greetings():
    print("Hello, how are you?")
    
# below we call the function by use of it's name.
greetings()

print('============================')
# Additional function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the numbers is: ", sum)

addition()

print('=============================')
# create a function that able to multiply three values
def multiplication():
    num3 = 2
    num2 = 3
    num1 = 10
    product = num3 * num2 * num1
    print("The product of the numbers is: ", product)

multiplication()

print('============================')
# below is a division function
def division():
    number1 = int(input("Enter the first number"))
    number2 = int(input("Enter the second number"))
    quotient = number1 / number2
    print("The quotient of the number is: ", quotient)
    print("-------")

for function in range(4):
 division()


print('==========================')
