# 1. Print numbers from 1 to 10 using a for loop
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# 2. Print even numbers from 1 to 20 using a while loop
print("Even numbers from 1 to 20:")
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num, end=" ")
    num += 1
print("\n")

# 3. Use break to stop the loop when number is 5
print("Break when number is 5:")
for i in range(10):
    if i == 5:
        break
    print(i)
print("\n")

# 4. Use continue to skip printing number 3
print("Continue when number is 3:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
print("\n")

# 5. Loop with else
print("For loop with else:")
for i in range(3):
    print(f"Looping: {i}")
else:
    print("Loop completed without break.")
print("\n")

# 6. Sum of numbers 1 to 5 using a while loop
print("Sum of numbers 1 to 5:")
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print("Total sum:", total)
