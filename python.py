x = 10               # integer
y = 3.5              # float
name = "Alice"       # string
is_valid = True      # boolean
numbers = [1, 2, 3]  # list
coordinates = (3.5, 7.2)  # tuple
person = {'name': 'Alice', 'age': 30}  # dictionary

print(f"x = {x}, type: {type(x)}")
print(f"y = {y}, type: {type(y)}")
print(f"name = {name}, type: {type(name)}")
print(f"is_valid = {is_valid}, type: {type(is_valid)}")
print(f"numbers = {numbers}, type: {type(numbers)}")
print(f"coordinates = {coordinates}, type: {type(coordinates)}")
print(f"person = {person}, type: {type(person)}")


# Example of an if-else statement
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Example of a for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Define a function that takes two arguments and returns their sum
def sum_numbers(a, b):
    return a + b

# Example of how to call this function
result = sum_numbers(3, 5)
print(f"The sum of 3 and 5 is: {result}")

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create a dictionary of person details
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Accessing elements
print("List:")
print(f"First number: {numbers[0]}")
print()

print("Dictionary:")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print()

# Modifying elements
numbers[0] = 10  # Update the first element in the list
person['age'] = 31  # Update the age in the dictionary

print("Modified List:")
print(numbers)
print()

print("Modified Dictionary:")
print(person)
print()

# Adding elements
numbers.append(6)  # Add a new number to the list
person['gender'] = 'Female'  # Add a new key-value pair to the dictionary

print("List after adding element:")
print(numbers)
print()

print("Dictionary after adding element:")
print(person)
print()

# Removing elements
numbers.remove(3)  # Remove a specific number from the list
person.pop('city')  # Remove a key-value pair from the dictionary

print("List after removing element:")
print(numbers)
print()

print("Dictionary after removing element:")
print(person)

# Example of exception handling using try, except, and finally blocks

# Function to divide two numbers and handle ZeroDivisionError
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result of {a} divided by {b} is: {result}")
    finally:
        print("Execution of divide_numbers function completed.")

# Example of usage
divide_numbers(10, 2)   # This will execute normally
print()

divide_numbers(10, 0)   # This will trigger a ZeroDivisionError
print()

divide_numbers("10", "2")  # This will trigger a TypeError

# Example of importing and using the math module
import math

# Using mathematical functions from math module
radius = 5
area = math.pi * radius ** 2
square_root = math.sqrt(25)

print(f"Area of a circle with radius {radius} is: {area}")
print(f"Square root of 25 is: {square_root}")

# Example of reading from a file and printing its content

# Define the file path (change this to your file's path)
file_path = 'sample.txt'

try:
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()
        
        # Print each line
        for line in lines:
            print(line.strip())  # .strip() removes the newline character '\n'
            
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
except IOError as e:
    print(f"Error: Unable to read the file '{file_path}'. Error: {e}")

# Example of writing a list of strings to a file

# Define the file path where you want to write the data
file_path = 'output.txt'

# List of strings to write to the file
data = [
    "First line",
    "Second line",
    "Third line",
    "Fourth line"
]

try:
    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Write each string in the list to the file
        for line in data:
            file.write(line + '\n')  # Add '\n' to write each string on a new line
            
    print(f"Data successfully written to '{file_path}'.")
    
except IOError as e:
    print(f"Error: Unable to write to the file '{file_path}'. Error: {e}")
