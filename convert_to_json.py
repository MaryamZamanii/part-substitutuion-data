import pandas as pd

# File paths
excel_path = r"C:\Users\sesa778113\Desktop\part-substitution-app\backend\parts.xlsx"
json_path = r"C:\Users\sesa778113\Desktop\part-substitution-app\backend\parts.json"

# Read Excel
df = pd.read_excel(excel_path)

# Set column headers
df.columns = ["part_number", "option_1", "option_2", "option_3", "comment"]

# Fill blanks with empty string
df = df.fillna("")

# Convert to JSON
df.to_json(json_path, orient="records", indent=4)

print("✅ parts.json updated from parts.xlsx")