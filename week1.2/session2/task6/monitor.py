# Week 1.2, Session 2: Task 6
### Step 1: Get User Inputs
### Step 2: Evaluate Operating Conditions
#### Temperature
#### Pressure
### Step 3: Determine Status


temperature=int(input("Please enter the machine's temperature in degrees Celsius"))
pressure=int(input("Please enter the machine's pressure in PSI"))
operational_status=int(input("Please enter the machine's operational status (1 for operating, 0 for stopped)"))

safe_temperature=True
safe_pressure=True

if temperature>80:
  print("The temperature is too high and recommended shutting down the machine.")
  safe_temperature=False
elif temperature<50:
  print("The machine temperature is low and no action is needed.")
else:
  print("The temperature is within safe limits")

if pressure>100:
  print("High pressure is detected and maintenance recommended.")
  safe_pressure=False
elif pressure<70:
  print("The pressure is low and the system is operating normally.")
else:
  print("The pressure is stable.")

if operational_status==1:
  if safe_pressure==False or safe_temperature==False:
    print("The machine is running in unsafe conditions and recommend shutting it down.")
  else:
    print("The machine is running normally.")
else:
  print("Machine is stopped and no immediate action is needed.")


