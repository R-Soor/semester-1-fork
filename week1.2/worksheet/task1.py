# Worksheet 1.2: Task 1 Solution
import sys
is_valid=True

try:
    grade=int(input("Please enter a grade in the range 0 to 100"))
except ValueError:
    is_valid=False
    print("Error: Grade must be an integer between 0 and 100")
    sys.exit()
if grade>100 or grade<0:
    print("Error: Grade must be an integer between 0 and 100")
    sys.exit()
elif grade>=70:
    print(f"{grade} is a Distinction")
elif grade<=39:
    print(f"{grade} is a Fail")
else:
    print(f"{grade} is a Pass")
