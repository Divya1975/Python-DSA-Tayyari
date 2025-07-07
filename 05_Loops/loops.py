```python
# for loop
print("For Loop:")
for i in range(1, 6):
    print(i)

# while loop
print("\nWhile Loop:")
i = 1
while i <= 5:
    print(i)
    i += 1

# break example
print("\nBreak Example:")
for i in range(10):
    if i == 5:
        break
    print(i)

# continue example
print("\nContinue Example:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# pass example
print("\nPass Example:")
for i in range(3):
    pass

# else with loop
print("\nElse with loop:")
for i in range(3):
    print(i)
else:
    print("Loop completed.")
