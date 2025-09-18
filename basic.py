# Student Grade Calculator

# Input
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

# Control Flow with Operators
if marks >= 90:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C"

# Function
def result(name, grade):
    return f"{name} got Grade {grade}"

# Loop to display stars for grade
for i in range(len(grade)):
    print("*", end="")

print("\n", result(name, grade))
