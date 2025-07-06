# Conditional Statements in Python

Conditional statements are used to make decisions in code.

## 1. if Statement
x = 10
if x > 5:
    print("x is greater than 5")

## 2. if-else Statement
age = 17
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
    
## 3. if-elif-else Statement
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

## 4. Nested if
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
