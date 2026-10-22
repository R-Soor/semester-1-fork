
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name: Roshan Soor
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }

    rate=conversion_rate[from_currency][to_currency]
    final_conversion=amount*rate
    final_conversion=round(final_conversion, 2)

    return final_conversion
amount=float(input("Please enter the amount you want to convert"))
if amount<=0:
    print(0.0)
else:
    original_currency=input("What currency is this value currently in")
    new_currency=input("What currency would you like to convert it to")
    print(currency_converter(amount, original_currency, new_currency))