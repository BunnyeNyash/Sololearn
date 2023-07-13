# Prompt user for temperature in celsius
temp = input("Your temperature in °Celsius: ")

try:
    temp = int(temp)

    if temp >= 100:
        print("Boiling")
    else:
        print("Not Boiling")

except ValueError:
    print("Please enter a numerical value")
