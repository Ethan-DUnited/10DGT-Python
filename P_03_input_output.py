# Ask the user for their name
# Ask the user for their favourite number (integer)
# Double, half, and square the user's favourite number
# Greet the user
# Output the results of doubling, halfing and squaring the user's favourite integer

# Ask the user for their name:
username = input("What is your name? ")

# Ask the user for their favourite number (integer):
fav_num = int(input("What is your favourite number? "))

# Double, half and square the user's favourite number:
double = fav_num * 2
half = fav_num / 2
square = fav_num * fav_num

# Greet the user:

print(f"\nHi {username}, your favorite number is {fav_num}")

# Output the results of doubling, halfing and squaring the user's favourite integer:
print(f" Double {fav_num} is {double}")
print(f" Half {fav_num} is {half}")
print(f" Square {fav_num} is {square}")
print()
print("Have a nice day!")
