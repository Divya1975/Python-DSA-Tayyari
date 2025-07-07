# Loops in Python

Loops are used to repeat a block of code multiple times.

## 1. for loop
Used to iterate over a sequence (list, string, range, etc.)

for i in range(5):
    print(i)
    
## 2. while loop
Repeats as long as the condition is True.
i = 0
while i < 5:
    print(i)
    i += 1
    
## 3. break, continue, pass
break: Exits the loop early

continue: Skips the current iteration

pass: Placeholder, does nothing

## 4. else with loops
Executes when loop finishes normally (without break).
for i in range(3):
    print(i)
else:
    print("Loop finished")

