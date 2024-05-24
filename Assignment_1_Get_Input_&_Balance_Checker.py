# Assignment 1 - Fence Cost Calculator
# Author: Ethan du Toit
# Version: V2

print() 
# Greet the user
print("🎉 WELCOME TO THE FENCE COST CALCULATOR! 🎉")

print() 
# Ask user for width, length & cost per metre
print("Please enter your width, length & cost per metre values of your fence into the calculator: ")
print()


def error_checker(question):
    done = False
    error = "Please enter a valid number (must be more than zero)"
    while not done:
        print(question)
        try:
            num = float(input())
            if num > 0:
                done = True
            else:
                print(error)
        except ValueError:
            print(error)
    return(num)


# Main routine:
width = error_checker("Please enter your WIDTH value: ")
print()
print(f"⚪️ The width you entered is {width}.")

print()

length = error_checker("Please enter your LENGTH value: ")
print()
print(f"⚪️ The width you entered is {length}.")

print()

costpm = error_checker("Please enter your COST PER METRE value: ")
print()
print(f"⚪️ The width you entered is {costpm}.")