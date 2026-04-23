import json

FILE = "database.json"

# LOAD 
def load_data():
    with open(FILE, "r") as f:
        return json.load(f)

# READ 
def get_chips():
    data = load_data()
    for snack in data["snacks"]:
        if snack["category"] == "chips":
            print(snack)

def sales_grade10():
    data = load_data()
    for sale in data["sales"]:
        for student in data["students"]:
            if student["student_id"] == sale["student_id"]:
                if student["grade_level"] == 10:
                    print(sale)

def total_quantity():
    data = load_data()
    total = 0
    for sale in data["sales"]:
        total += sale["quantity"]
    print("Total quantity:", total)


# QUESTIONS 
def most_popular_snack():
    data = load_data()
    count = {}

    for sale in data["sales"]:
        sid = sale["snack_id"]
        count[sid] = count.get(sid, 0) + sale["quantity"]

    max_id = max(count, key=count.get)

    for snack in data["snacks"]:
        if snack["snack_id"] == max_id:
            print("Most popular snack:", snack["name"])


def top_student():
    data = load_data()
    count = {}

    for sale in data["sales"]:
        sid = sale["student_id"]
        count[sid] = count.get(sid, 0) + 1

    max_id = max(count, key=count.get)

    for student in data["students"]:
        if student["student_id"] == max_id:
            print("Top student:", student["name"])


def average_spent():
    data = load_data()
    total = 0

    for sale in data["sales"]:
        total += sale["total_price"]

    avg = total / len(data["sales"])
    print("Average spent:", avg)


#  MAIN 
    if _name_ == "_main_":
    print("Snacks in chips category:")
    get_chips()

    print("\nSales by Grade 10:")
    sales_grade10()

    print()
    total_quantity()

    print()
    most_popular_snack()
    top_student()
    average_spent()