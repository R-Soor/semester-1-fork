"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""

travel_cost_input = float(input("Travel cost in pounds: "))
food_cost_input = float(input("Food cost in pounds: "))
accommodation_cost_input = float(input("Accommodation cost in pounds: "))
total_cost=travel_cost_input+food_cost_input+accommodation_cost_input
avg_cost=total_cost/3
print(f"The travel cost is £{travel_cost_input:.2f}, the food cost is £{food_cost_input:.2f}, the acommodation cost is £{accommodation_cost_input:.2f}, the total cost is £{total_cost:.2f}, the average cost per category is £{avg_cost:.2f}")
