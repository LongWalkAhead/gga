"""
Task 1: Create functions for each arithmetic operation.

Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

to do
    
    setup if statement if user wants to multiply, add, sub, or divide
    if they chose to add use num1 and num2 as factors to add together and print result

"""
def addition(num1, num2):
    print(num1 + num2)

def subtraction (num1, num2):
    print(num1-num2)

def multiplication (num1, num2):
    print(num1*num2)
    
def divison (num1, num2):
    print(num1 // num2)
    


response = input("would you like to add, subtract, multiply, or divide?")
num1 = int(input("what is the first number?"))
num2 = int(input("what is the second number?"))
print(response, num1, num2)

if response == "add":
    addition(num1, num2)

if response == "subtract":
    subtraction(num1, num2)

if response == "divide":
    divison(num1, num2)

if response == "multiply":
    multiplication(num1, num2)
