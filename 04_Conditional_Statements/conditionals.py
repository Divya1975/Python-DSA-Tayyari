# Simple if statement
marks = 85
if marks >= 80:
    print("Great job!")

# if-else statement
age = 17
if age >= 18:
    print("Adult")
else:
    print("Minor")

# if-elif-else statement
temp = 32
if temp > 35:
    print("Hot")
elif temp >= 20:
    print("Normal")
else:
    print("Cold")

# Nested if statement
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
