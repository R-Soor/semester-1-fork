halt=False
try:
    num1=int(input("Please enter your first number"))
except ValueError:
    print("That is not a number")
    halt=True

try:
    num2=int(input("Please enter you second number"))
except ValueError:
    print("That is not a number")
    halt=True

if halt==False:
    print(num1*num2)
