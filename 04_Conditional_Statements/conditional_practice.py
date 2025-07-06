# Q1. Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q2. Largest of 3 numbers
a, b, c = 5, 8, 3
if a >= b and a >= c:
    print("a is largest")
elif b >= a and b >= c:
    print("b is largest")
else:
    print("c is largest")

# Q3. Pass/Fail
score = 40
if score >= 33:
    print("Pass")
else:
    print("Fail")
