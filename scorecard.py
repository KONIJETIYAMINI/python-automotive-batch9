# Function to check pass or fail
def check_result(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"

# Main program
subject = input("Enter subject name: ")
marks = int(input("Enter marks: "))

result = check_result(marks)

print("Subject:", subject)
print("Marks:", marks)
print("Result:", result)
