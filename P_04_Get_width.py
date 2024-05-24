# Get Width Program
# Author: Ethan du Toit
# Date: 17 May 2024
# Version: V1

# Ask user for width and loop until they enter a number more than zero.

error = "Please enter a number that is more than zero\n"

try:
    while True:
        width = float(input("Width: ")) # Ask the user for a number

        if width > 0: # Check that the number is more than zero
            break
        else:
            print(error)

except ValueError:
    print(error)


