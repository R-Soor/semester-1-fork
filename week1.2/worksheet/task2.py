# Worksheet 1.2: Task 2 Solution
def read_numbers():
    """
    Prompts the user to enter a series of numbers on a single line,
    separated from each other by spaces.

    Returns a list of float values corresponding to the numbers that were
    input by the user.
    """
    line = input("Enter some numbers, separated by spaces: ")
    numbers = [float(item) for item in line.split()]
    return numbers

max=0
min=0
sum=0
numbers=read_numbers()
for i in range (0, len(numbers)-1):
    if i==0:
        max=numbers[i]
        min=numbers[i]
    else:
        if numbers[i]>max:
            max=numbers[i]
        elif numbers[i]<min:
            min=numbers[i]
    sum+=numbers[i]

print(f"Minimum = {min}")
print(f"Maximum = {max}")
print(f"Mean = {sum/
#
# 
# 
# len(numbers)}")