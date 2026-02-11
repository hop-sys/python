# functions with parameters
# Parameters are values that get passed as arguements given to a function insude of the parenthesis


def greeting(name):
    print(f"{name} How are you? Hope everything is fine.")

greeting("Hope")
greeting("Malia")

print('==========================')
def message(names):
    print(f"Hello {names} We shall be having a general meeting on date...Please avail yourself.")

message("Frank")
message("Jesca")


print('==========================')
# create a function that accepts parameters to add two numbers
def addition(num1, x):
    sum = num1 + x
    print("The sum is ", sum)

addition(10, 20)
addition(15, 3)