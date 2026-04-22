# Mini-Dataset Project
# Scenario: Scores of 3 Miss Universe finalists across 5 categories

# Rows = Candidates (Philippines, USA, Venezuela)
# Columns = Categories (Swimsuit, Evening Gown, Q&A, National Costume, Interview)

scores = [
    [9.4, 9.6, 9.8, 9.5, 9.7],  # Philippines
    [9.2, 9.5, 9.6, 9.4, 9.5],  # USA
    [9.1, 9.3, 9.5, 9.2, 9.4]   # Venezuela
]

# 1. Print a specific value (Philippines' Q&A score)
print("Philippines' Q&A score:", scores[0][2])

# 2. Update a specific value (USA’s Interview score changed)
scores[1][4] = 9.6
print("Updated USA Interview score:", scores[1][4])

# 3. Summarize: Compute the average score of each candidate
for i, country in enumerate(["Philippines", "USA", "Venezuela"]):
    avg = sum(scores[i]) / len(scores[i])
    print(f"Average score for {country}: {avg:.2f}")

# Reflection:
# I chose this dataset because Miss Universe scoring is exciting and easy to understand.
# A 2D array helps organize the scores of each contestant in different categories.
# It makes it simple to compare their performance, update scores, and find averages clearly.