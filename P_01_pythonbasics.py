# Python Basics
# Author: Ethan du Toit
# Date: 3 & 8 May 2024  

say_hello = "hello"
print(say_hello)

# -------------------------------------

# Adding strings together is called concatenation
sum = "5" + "5"
print(sum)

# -------------------------------------

sum =5 + 5
print(sum)

# -------------------------------------

# Strings are treated as text. Note colour and speech marks
string_eg1 = "This is a string"
string_eg2 = "7"

# -------------------------------------

# Integers are numbers with no decimal point.
# If you add two integers together, it will both become an integer.
# If you add an integer and a float together, it will become a float.
integer_eg = 7

# -------------------------------------

# Floats are numbers with a decimal point
float_eg = 7.25

# -------------------------------------

# Boolean values are either True or False. (If statements)
bool_eg1 = True
bool_eg2 = False

# -------------------------------------

# You can then print thse commands.
print (string_eg1),(string_eg2)
print (integer_eg)
print (float_eg)
print (bool_eg1),(bool_eg2)

# -------------------------------------

# INDENTING: Used for loops, if statements & functions
# There are two types of loops: 
# - a WHILE loop
# - a FOR loop

# EXAMPLE OF A WHILE LOOP:
keep_going = ""
while keep_going == "":
    print("looping")
    print("still looping")

    keep_going = input("Again?")

print("all done")

# Before loop, there is a colon ;, and then indentation takes place.

# -------------------------------------

# Functions
# 1. always start with DEF (define)
# 2. Put (): after function name
# 3. Then indent

def intro():
    print("Welcome")
    print()             #Empty print statements are line breaks
    print("Instructions go here")
    return ""           # You are returning (displaying / using) all items in the code

# Main routine
intro() # This calls the function so that we can use it


