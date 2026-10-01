"""Advanced Task 5: Safe Divider
- Ask for a numerator and a denominator.
- Convert both inputs to integers and divide them to get a result.
- Use try/except to catch both non-numeric input and division by zero, giving useful messages for each case.
- Only print the final answer when the calculation succeeds.
"""
valid_inputs=False
while valid_inputs==False:
    valid_numerator=False
    while valid_numerator==False:
        valid_numerator=True
        try:
            numerator_input = int(input("Enter the numerator: "))
        except ValueError:
            print("Please enter your numerator as an integer")
            valid_numerator=False
    valid_denominator=False
    while valid_denominator==False:
        valid_denominator=True
        try:
            denominator_input = int(input("Enter the denominator: "))
            if denominator_input==0:
                print("Can't divide by 0")
                valid_denominator=False
        except ValueError:
            print("Please enter your denominator as an integer")
            valid_denominator=False
    if valid_denominator and valid_numerator:
        valid_inputs=True
division=numerator_input/denominator_input
print(f"The result of your division is {division}")

    


