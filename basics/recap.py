
# -------------------------------
# Variables and Basic Datatypes
# -------------------------------
name = input("Enter your name: ")          # String input
age = int(input("Enter your age: "))       # Integer input (type conversion)
salary = float(input("Enter your salary: "))  # Float input

# Boolean datatype
is_employee = True

# -------------------------------
# Output using String Formatting
# -------------------------------
print("\n--- User Details ---")
print("Name: %s" % name)                  # %s for string
print("Age: %d" % age)                    # %d for integer
print("Salary: %.2f" % salary)            # Float with 2 decimals

# -------------------------------
# Operators
# -------------------------------
bonus = salary * 0.10                     # Arithmetic operator
total_salary = salary + bonus

print("Bonus: %.2f" % bonus)
print("Total Salary: %.2f" % total_salary)

# -------------------------------
# Conditional Control Statements
# -------------------------------
if age >= 18:
    print("Status: Eligible to work")
else:
    print("Status: Not eligible to work")

# -------------------------------
# Loop Control Statements
# -------------------------------
print("\nCounting using for loop:")
for i in range(1, 6):                      # for loop
    print(i)

print("\nUsing while loop:")
count = 1
while count <= 3:
    print("Count:", count)
    count += 1

# -------------------------------
# break, continue, pass
# -------------------------------
print("\nDemonstrating break and continue:")
for num in range(1, 6):
    if num == 3:
        continue       # Skip number 3
    if num == 5:
        break          # Stop loop at 5
    print(num)

# pass statement example
if is_employee:
    pass               # Placeholder (does nothing)

# -------------------------------
# Data Structures
# -------------------------------
numbers = [1, 2, 3]                     # List
person = {"name": name, "age": age}     # Dictionary
unique_ids = {101, 102, 103}             # Set

print("\nList:", numbers)
print("Dictionary:", person)
print("Set:", unique_ids)

# -------------------------------
# End of Program
# -------------------------------
print("\nProgram executed successfully.")
