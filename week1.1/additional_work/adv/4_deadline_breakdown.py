"""Advanced Task 4: Deadline Breakdown
- Ask how many minutes remain until an assignment deadline.
- Use integer division and modulo to convert this number into days, hours, and minutes.
- Present the result using a formatted string such as "2 days, 3 hours, 15 minutes remaining".
- Extension: handle negative input by printing a warning that the deadline has already passed.
"""
valid_input=False
while valid_input==False:
    valid_input=True
    try:
        minutes_remaining_input = int(input("Minutes remaining until the deadline: "))
    except ValueError:
        print("Please enter input as an integer")
        valid_input=False

days=0
hours=0
minutes=0
if minutes_remaining_input<0:
    print("Deadline has already passed")
else:
    if minutes_remaining_input//1440>=1:
        days=minutes_remaining_input//1440
        minutes_remaining_input=minutes_remaining_input%1440
    if minutes_remaining_input//60>=1:
        hours=minutes_remaining_input//60
        minutes_remaining_input=minutes_remaining_input%60
    minutes=minutes_remaining_input
    print(f"{days} days, {hours} hours and {minutes_remaining_input} minutes remaining")
# TODO: convert the input to an integer
# TODO: calculate whole days, leftover hours, and remaining minutes
# TODO: print the breakdown using f-strings
# Extension: detect negative values and print a warning instead
