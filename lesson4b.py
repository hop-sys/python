# Loops ->sometimes we may need to do a piece of work a number of repeated times and in such cases we may use loops
# A loop is control structure that allows us to execute a block of code repeatedly untill a certain condition is met
# There are 2 types of loops in python i.e The for loop and The while loop
# below is the syntax of a for loop in python:
"""
for variable in range(n):
  #block of code to be executed
"""


for greeting in range(5):
    print("Hello Moses", greeting)

    print("==========================")

    for number in range(10, 20):
      print(number)

      print('=======================')
#   find the even numbers in the range of 50 to 71
for number in range (50, 71, 2):
   print(number)

   print('==========================')
#    create a python prograam that prints the odd numbers from 100 to 150
for number in range (101, 150, 2):
   print(number)


   print('=========================')
#    create a programme that prints the multiples of three starting from 201 to 150
for number in range (201, 149, -3):
   print(number)

   print('========================')
#    create a python programme that prints the leaps years between 2000 and 2024
for number in range (2000, 2025, 4):
   print(number)
