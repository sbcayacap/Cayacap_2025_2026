import json

database = {
    "students": [
        {
            "student_id": 1,
            "name": "Perpetiel Sue D. Villas",
            "age": 14,
            "fav_subj": "Math 2",
            "fav_color": "Purple",
            "fav_song": "You'll be in my Heart - NIKI"
        },
        {
            "student_id": 2,
            "name": "Anne Venice C. Villarta",
            "age": 14,
            "fav_subj": "ADTech",
            "fav_color": "Navy Blue",
            "fav_song": "Smoking Out the Window - Silk Sonic"
        },
        {
            "student_id": 3,
            "name": "Maria Chela C. Gallano",
            "age": 14,
            "fav_subj": "Biology",
            "fav_color": "Crimson",
            "fav_song": "All I Need to Hear - The 1975"
        },
        {
            "student_id": 4,
            "name": "Raymundo III C. Sarabia",
            "age": 14,
            "fav_subj": "ValEd",
            "fav_color": "Cyan",
            "fav_song": "Happiness - Rex Orange County"
        },
        {
            "student_id": 5,
            "name": "Shekinah Joyce B. Cayacap",
            "age": 14,
            "fav_subj": "Biology",
            "fav_color": "Purple",
            "fav_song": "Show Yourself - Frozen"
        },
        {
            "student_id": 6,
            "name": "Andreia Celine C. Morales",
            "age": 13,
            "fav_subj": "Chemistry",
            "fav_color": "Blue",
            "fav_song": "Killing in the Name - Rage Against the Machine"
        }
    ]
}

for student in database["students"]:
    print("ID:", student["student_id"])
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Favorite Subject:", student["fav_subj"])
    print("Favorite Color:", student["fav_color"])
    print("Favorite Song:", student["fav_song"])
    print("-------------------------")

