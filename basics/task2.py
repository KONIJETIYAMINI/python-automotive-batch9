# Take user inputs
name = input("Enter your name: ")          # String
age = int(input("Enter your age: "))       # Convert to integer
salary = float(input("Enter your salary: "))  # Convert to float

# Display information using string formatting
print("Name: %s" % name)
print("Age: %d years" % age)
print(f"Salary: %.2f" % salary)
