"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }
states_list=list(states)
systime = 0

maxtime = int(input("Input number of steps (>0)"))  # read an integer number of steps (>0)
print(states["red"])
states_list_index=0
light_time = 0
state = "red"
prev_state = ""
print(states_list)
while systime<maxtime:
    if prev_state=="":
        light_time=states[state]
        prev_state=state

    print(f"Time {systime:03} State {state}")
    light_time-=1
    systime+=1

    if light_time==0:
        states_list_index+=1
        if states_list_index>=len(states_list):
            states_list_index=0
        state = states_list[states_list_index]
        prev_state=""


# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14