"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""
destination = input("Where are you going to? ")

valid_distance=False
while valid_distance==False:
  valid_distance=True
  try:
    distance_miles_input = float(input("How many miles will you travel? "))
    if distance_miles_input<=0:
      valid_distance=False
  except:
    print("Please enter distance as a decimal or integer")
    valid_distance=False
valid_time=False
while valid_time==False:
  valid_time=True
  try:
    time_hours_input = float(input("How many hours will the journey take? "))
    if time_hours_input<=0:
      valid_time=False
  except:
    print("Please enter time as a integer or decimal")
avg_speed=distance_miles_input/time_hours_input
print(f"The approximate average speed for the journey to {destination} will be {avg_speed:.2f}mph.")

