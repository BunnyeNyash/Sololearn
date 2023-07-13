# Prompt the user for percentage of humidity
humidity = input("Humidity Percent: ")

try:
    humidity = int(humidity)

    if humidity >= 40 and humidity <= 60:
        print("norm")
    else:
        print()

except ValueError:
    print("Please input a numerical Value")
