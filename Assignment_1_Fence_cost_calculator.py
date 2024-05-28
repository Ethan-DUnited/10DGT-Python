# Assignment 1 - Fence Cost Calculator
# Author: Ethan du Toit
# Version: V1

# Ask user for width, length & cost per metre

error = "Please enter a number that is more than zero"

try:
    while True:
        width = float(input("Width: "))
        length = float(input("Length: "))
        costpm = float(input("Cost per metre: "))

        if width > 0:
            break
        elif length > 0:
            break
        elif costpm > 0:
            break

        else:
            print(error)

except ValueError:
    print(error)

