numbers = [10, 25, 3, 99, 56]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)