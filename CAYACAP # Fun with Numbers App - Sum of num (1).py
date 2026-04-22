# Fun with Numbers App - Sum of numbers up to your age

print("Welcome to the Fun with Numbers App!")

# Input handling: ensure a positive age
age = 0
while age <= 0:
    age = int(input("Please enter your age: "))
    if age <= 0:
        print("Invalid input. Enter a positive number.")

# Compute the sum
total = 0
for i in range(1, age + 1):
    total += i

# Display the result
print(f"The sum of all numbers from 1 to {age} is: {total}")
