#KISAKYE MARTHA JANRPHER
#21/U/10006/EVE
#2100710006

#EXCEPTION AND FILE HANDLING
#Exception handling 
#xception handling in Python is a programming mechanism that allows you to handle errors or exceptional situations gracefully 
#and prevent your program from crashing. 

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
finally:
    print("End of the program.")
    
#File handling
#File handling in Python refers to the process of working with files, including reading from and writing to files. 
# Python provides built-in functions and methods that allow you to interact with files in a convenient and straightforward manner.

file_path = "example.txt"
# Open the file in write mode
with open(file_path, "w") as file:
    file.write("Hello, this is a line written to the file.\n")
    file.write("This is another line.\n")

# Example of reading from a file
with open(file_path, "r") as file:
    contents = file.read()
    print(contents)
    
#Example for both
def sum_integers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            total_sum = 0
            for line in file:
                try:
                    number = int(line.strip())
                    total_sum += number
                except ValueError:
                    print(f"Error: Non-integer value found in the file: '{line.strip()}'")
            return total_sum
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

# Test the sum_integers_from_file function
filename = "data.txt"
result = sum_integers_from_file(filename)
if result is not None:
    print(f"The sum of integers in '{filename}' is: {result}")