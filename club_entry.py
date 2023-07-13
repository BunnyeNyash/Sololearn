# Prompt patron for name
name = input("Your name? ")

# Prompt patron for age
try:
    age = int(input("Your age: "))

except ValueError:
    print("Please input a numerical value")

if age >= 18:
    print("Welcome", name)
else:
    print("Sorry")
