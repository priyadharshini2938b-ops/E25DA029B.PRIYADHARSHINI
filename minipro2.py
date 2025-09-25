import pandas as pd
data = {
    "Name": ["Megna", "Manoj", "Vishwa", "Priya"],
    "Age": [21, 31, 20, 22],
    "Department": ["Sales", "Manager", "Finance", "Marketing"],
    "Salary": [20000, 70000, 3000, 65000]}
result = pd.DataFrame(data)
print(result)
result.to_csv("minipro2.csv", index=False)

print("Data saved to sample_data.csv")
