# Worksheet 1.2: Task 2 Solution
import sys
def read_numbers():
    """
    Prompts the user to enter a series of numbers on a single line,
    separated from each other by spaces.

    Returns a list of float values corresponding to the numbers that were
    input by the user.
    """
    line = input("Enter some numbers, separated by spaces: ")
    if line=="":
        sys.exit("Error: no numbers provided")
    numbers = [float(item) for item in line.split()]
    return numbers

max=0
min=0
sum=0
sort_list=[]
numbers=read_numbers()
for i in range (0, len(numbers)):
    if i==0:
        max=numbers[i]
        min=numbers[i]
        sort_list.append(numbers[i])
    else:
        if numbers[i]>max:
            max=numbers[i]
        elif numbers[i]<min:
            min=numbers[i]
        has_insterted=False
        index_to_sort=0
        while has_insterted==False:
            if numbers[i]>=sort_list[index_to_sort]:
                index_to_sort+=1
                if index_to_sort>=len(sort_list):
                    sort_list.append(numbers[i])
                    has_insterted=True
            else:
                sort_list.insert(index_to_sort, numbers[i])
                has_insterted=True
    sum+=numbers[i]

print(f"Sorted {sort_list}")
print(f"Minimum = {min}")
print(f"Maximum = {max}")
print(f"Mean = {sum/len(numbers)}")
if len(sort_list)%2==1:
    middle=(len(sort_list)+1)//2
    print(middle)
    median=sort_list[middle-1]
else:
    middle=(len(sort_list))//2
    median = ((sort_list[middle-1])+(sort_list[middle]))/2
print(f"Median = {median}")
#
# 
# 
