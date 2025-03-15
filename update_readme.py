import os
import re

# Define the folder where your solutions are stored
leetcode_path = "LeetCode-Solutions"

# Define difficulty categories
categories = {"Easy": 0, "Medium": 0, "Hard": 0}

# Traverse through each problem folder and count solutions
for root, dirs, files in os.walk(leetcode_path):
    for file in files:
        if file.endswith(".py") or file.endswith(".sql"):  # Adjust based on your solution format
            if "Easy" in root:
                categories["Easy"] += 1
            elif "Medium" in root:
                categories["Medium"] += 1
            elif "Hard" in root:
                categories["Hard"] += 1

# Calculate total solved problems
total_solved = sum(categories.values())

# Update README file
readme_path = "README.md"

with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

# Use regex to update the Progress Tracker table
updated_readme = re.sub(
    r"(\| \*\*Easy\*\* +\| )\d+",
    rf"\1{categories['Easy']}",
    readme_content
)

updated_readme = re.sub(
    r"(\| \*\*Medium\*\* +\| )\d+",
    rf"\1{categories['Medium']}",
    updated_readme
)

updated_readme = re.sub(
    r"(\| \*\*Hard\*\* +\| )\d+",
    rf"\1{categories['Hard']}",
    updated_readme
)

updated_readme = re.sub(
    r"(\| \*\*Total\*\* +\| )\d+",
    rf"\1{categories['Total']}",
    updated_readme

)

# Write the updated content back to README
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(updated_readme)

print("README updated successfully!")
