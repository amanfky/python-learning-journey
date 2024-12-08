# Python Basics - Day 1

# Variables and Data Types

name = "Amanuel"
age = 25
height = 5.9
is_student = True

print(f"Hello, my name is {name}. I am {age} years old and {height} feet tall.")

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

for i in range(1,6):
    print(f"Counting: {i}")


def greet_user(username = "Guest"):
    print(f"Welcome, {username}!")

greet_user("Amanuel")
