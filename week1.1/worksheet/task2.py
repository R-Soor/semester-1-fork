"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Roshan Soor
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")
valid=True
try:
  monthly_savings = int(input("Please enter your monthly savings amount:"))
except ValueError:
  print("Invalid amount")
  valid=False

if valid==True:
  yearly_savings = 12*int(monthly_savings)
  print(f"You will save £{yearly_savings} per year")
  interest_savings = 1.008 * yearly_savings
  print(f"With interest, you will save £{interest_savings:.2f} per year")
