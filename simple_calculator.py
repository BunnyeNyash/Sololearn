# Prompt user for number
num1 = input("Your first number: ")
num2 = input("Your second number: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    
    # addition calculation
    result = num1 + num2
    print(result)
    
except ValueError:
    print("Please input a number")
