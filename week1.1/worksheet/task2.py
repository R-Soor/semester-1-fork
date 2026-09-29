"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Roshan Soor
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

monthly_savings = input("Please enter your monthly savings amount:")
if monthly_savings!=int(monthly_savings):
  print("Invaild Amount")
else:
  yearly_savings = 12*monthly_savings
  print(f"You will save £{yearly_savings} per year")
  interest_savings = 1.08 * yearly_savings
  print(f"With interest, you will save £{interest_savings} per year")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

