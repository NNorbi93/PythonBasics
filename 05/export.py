import json

import pandas as pd

print("""
open
window
""")

with open(file="data.json", mode="r", encoding="utf-8") as json_file:
    data = json.load(json_file)


print(data.get("database"))


print("{:<8} {:<15} {:<10}".format('Key', 'Label', 'Number'))
for k, v in data.get("database").items():
    label, num = v
    print("{:<8} {:<15} {:<10}".format(k, label, num))


print("\n"*50)
"""
df = pd.read_json(r'data.json')
df.to_csv(r'data.csv', index=None, header=False)
df.to_excel(r"data.xlsx", index=None, header=False)
print(df)
"""