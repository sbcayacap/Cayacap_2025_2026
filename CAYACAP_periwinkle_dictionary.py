name = input("Enter your name:")
age = input("Enter your age:")
subject = input("Enter your favorite subject:")

student = {
    "name": name,
    "age": age,
    "subject": subject
}

print("\nStudent Record:")
print("name",student["name"])
print("age", student["age"])