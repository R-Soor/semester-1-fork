# Week 1.2, Session 1: Task 1

# Create a shopping list

shopping = ["eggs", "milk", "flour", "carrots"]
print(shopping)

# We forgot something, so add it to list

shopping.append("bananas")
print(shopping)

# We bought something, so remove it from list

shopping.remove("eggs")
print(shopping)

# Replace bananas with grapes

index_bananas=shopping.index("bananas")
shopping[index_bananas]="grapes"
print(shopping)

# Add yoghurt, just after milk
index_milk=shopping.index("milk")
shopping.insert(index_milk+1,"yoghurt")
print(shopping)