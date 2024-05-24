# Assignment 1 - Fence Cost Calculator
# Author: Ethan du Toit
# Version: V1

print() 
# Greet the user
print("🎉 WELCOME TO THE FENCE COST CALCULATOR! 🎉")

print() 
# Ask user for width, length & cost per metre
print("Please enter your width, length & cost per metre values of your fence into the calculator: ")
print()


while True:
    error = "Please enter a number that is more than zero"
    done = False

    try: 
        while not done:
            width = float(input("Width: "))
            length = float(input("Length: "))
            costpm = float(input("Cost per metre: "))

            if width > 0:
                done = True
            elif length > 0:
                done = True
            elif costpm > 0:
                done = True

            else:
                print(error)
                

    except ValueError:
        print(error)
        continue

