
# List of 20 students with first name and surname
students = [
    ("Arjun", "Reddy"), ("Suman", "Das"), ("Kavya", "Sharma"), ("Rohit", "Verma"),
    ("Nikhil", "Patel"), ("Ananya", "Singh"), ("Suresh", "Kumar"), ("Meenal", "Gupta"),
    ("Arjun", "Kumar"), ("Pallavi", "Rao"), ("Vikas", "Sharma"), ("Sneha", "Patel"),
    ("Mahesh", "Reddy"), ("Divya", "Singh"), ("Karthik", "Iyer"), ("Anil", "Verma"),
    ("Pankaj", "Gupta"), ("Rina", "Das"), ("Ajay", "Patel"), ("Sita", "Rao")
]

seen = {}   # Dictionary to store first name as key and surname as value

# Loop through each student in the list
for name, surname in students:
    
    if name in seen:                 # Check if first name already exists
        if seen[name] != surname:    # Check if surname is different
            print("Found duplicate:")
            print(name, seen[name], "and", name, surname)
            break                    # Stop after finding first duplicate
    
    else:
        seen[name] = surname         # Store first name and surname in dictionary

