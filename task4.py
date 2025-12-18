import os

# Enter the directory path
path = input("Enter directory path: ")

# Create empty lists
files = []
directories = []

for item in os.listdir(path):  #returns all files and folders in the given directory.
    full_path = os.path.join(path, item)# Combines directory path and item name.

    if os.path.isfile(full_path):#Checks whether the item is a file. If yes, it executes the next line.
        files.append(item)
    elif os.path.isdir(full_path):#Checks whether the item is a directory (folder).
        directories.append(item)

# Display the results
print("\nFiles:")
for f in files:
    print(f)

print("\nDirectories:")
for d in directories:
    print(d)
