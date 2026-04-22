import json
from pathlib import Path

script_path = Path(_file_)
script_dir = script_path.parent
json_file = script_dir / 'database2.json'

# load json file
def load_data(filename=json_file):
    with open(filename, "r") as file:
        return json.load(file)

data = load_data()

snacks = data.get("snacks", [])
students = data.get("students", [])
sales = data.get("sales", [])


def get_snack_name(snack_id):
    for snack in snacks:
        if snack["snack_id"] == snack_id:
            return snack["name"]
    return "Unknown"


def get_student(student_id):
    for student in students:
        if student["student_id"] == student_id:
            return student
    return None



# Find all the snacks in chips
def find_chips():
    print("\nChips snacks:")
    for snack in snacks:
        if snack["category"] == "chips":
            print(snack)


# All the sales by gr10 students
def sales_grade_10():
    print("\nSales by Grade 10 students:")
    for sale in sales:
        student = get_student(sale["student_id"])
        if student and student["grade_level"] == 10:
            print(sale)


# The Total Quantity Sold Today
def total_quantity_today():
    if not sales:
        print("No sales data.")
        return

    today = sales[-1]["date"]
    total = 0

    for sale in sales:
        if sale["date"] == today:
            total += sale["quantity"]

    print("\nTotal quantity sold today:", total)



def update_snack_price(snack_id, new_price):
    for snack in snacks:
        if snack["snack_id"] == snack_id:
            snack["price"] = new_price
            print("Updated snack:", snack)
            return
    print("Snack not found.")


def update_student_grade(student_id, new_grade):
    for student in students:
        if student["student_id"] == student_id:
            student["grade_level"] = new_grade
            print("Updated student:", student)
            return
    print("Student not found.")


def update_sale_quantity(sale_id, new_quantity):
    for sale in sales:
        if sale["sale_id"] == sale_id:
            sale["quantity"] = new_quantity

            # Update Total price
            for snack in snacks:
                if snack["snack_id"] == sale["snack_id"]:
                    sale["total_price"] = new_quantity * snack["price"]

            print("Updated sale:", sale)
            return
    print("Sale not found.")


def delete_snack(snack_id):
    for snack in snacks:
        if snack["snack_id"] == snack_id:
            snacks.remove(snack)
            print("Snack removed.")
            return
    print("Snack not found.")


def delete_student(student_id):
    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            print("Student removed.")
            return
    print("Student not found.")


def delete_sale(sale_id):
    for sale in sales:
        if sale["sale_id"] == sale_id:
            sales.remove(sale)
            print("Sale removed.")
            return
    print("Sale not found.")



def most_popular_snack():
    counts = {}

    for sale in sales:
        snack_id = sale["snack_id"]
        counts[snack_id] = counts.get(snack_id, 0) + 1

    if not counts:
        print("No sales data.")
        return

    max_snack = max(counts, key=counts.get)
    print("\nMost popular snack:", get_snack_name(max_snack))


def top_spending_grade():
    grade_totals = {}

    for sale in sales:
        student = get_student(sale["student_id"])
        if student:
            grade = student["grade_level"]
            grade_totals[grade] = grade_totals.get(grade, 0) + sale["total_price"]

    if not grade_totals:
        print("No data.")
        return

    top_grade = max(grade_totals, key=grade_totals.get)
    print("Top spending grade level:", top_grade)


def most_sales_day():
    day_counts = {}

    for sale in sales:
        day = sale["day"]
        day_counts[day] = day_counts.get(day, 0) + 1

    if not day_counts:
        print("No data.")
        return

    max_day = max(day_counts, key=day_counts.get)
    print("Day with the highest number of sales:", max_day)


def top_student():
    counts = {}

    for sale in sales:
        student_id = sale["student_id"]
        counts[student_id] = counts.get(student_id, 0) + 1

    if not counts:
        print("No data.")
        return

    top_id = max(counts, key=counts.get)
    student = get_student(top_id)

    if student:
        print("Student with the most purchases:", student["name"])


def average_sale():
    if not sales:
        print("No data.")
        return

    total = sum(sale["total_price"] for sale in sales)
    avg = total / len(sales)

    print("Average amount spent per sale: ₱", round(avg, 2))


def trends():
    print("\nTrends noticed:")
    print("Piattos is the most popular snack, so the shop should stock more of it.")
    print("Grade 10 students spend the most, so the shop can target them with promotions.")
    print("Sales are the same each day, so the shop should keep inventory consistent.")


# Read
find_chips()
sales_grade_10()
total_quantity_today()

#reports
most_popular_snack()
top_spending_grade()
most_sales_day()
top_student()
average_sale()
trends() 