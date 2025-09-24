import pandas as pd
import random

f_names = ["Bob", "Sarah", "Hayden", "Ben", "Joe", "Ian", "Rachel", "Daniel", "Tom", "Sophie", "Lily", "Josh", "Mac", "Alex", "Isabelle", "Marie", "Emma"]
l_names = ["Smith", "Jones", "Johnson", "King", "Brown", "Williams", "Garcia", "Davis", "Miller", "Moore", "Anderson", "Foster", "German", "White", "Scott", "Fraker"]
years = ["Freshman", "Sophmore", "Junior", "Senior", "Super Senior"]
pathways = ["Early College", "Engineering", "Computer Science", "Business", "Marketing", "Early Childhood Education", "Culinary", "Bio Med", "Fine Arts", "Construction"]
names = []

for i in range(20_000):
    names.append(f"{random.choice(f_names)} {random.choice(l_names)}")

data = {
    "Name": names,
    "Age": [random.randint(14, 19) for _ in names],
    "GPA": [round(random.uniform(0.3, 4.5),2) for _ in names],
    "Credits_Completed": [random.randint(0,60) for _ in names],
    "Year": [random.choice(years) for _ in names],
    "Pathway": [random.choice(pathways) for _ in names]
}

pennData = pd.DataFrame(data)

print(pennData)
# print(names)

pennData.to_csv("pennData.csv", index = False)