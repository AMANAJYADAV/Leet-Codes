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

# Function to replace each category dynamically
def replace_category(match, category):
    return match.group(1) + str(categories[category]).rjust(2)  # Ensures formatting consistency

# Use regex to update progress tracker table
updated_readme = re.sub(
    r"(\|\s*\*\*Easy\*\*\s*\|\s*)\d+",
    lambda m: replace_category(m, "Easy"),
    readme_content
)

updated_readme = re.sub(
    r"(\|\s*\*\*Medium\*\*\s*\|\s*)\d+",
    lambda m: replace_category(m, "Medium"),
    updated_readme
)

updated_readme = re.sub(
    r"(\|\s*\*\*Hard\*\*\s*\|\s*)\d+",
    lambda m: replace_category(m, "Hard"),
    updated_readme
)

updated_readme = re.sub(
    r"(\|\s*\*\*Total\*\*\s*\|\s*)\d+",
    lambda m: m.group(1) + str(total_solved).rjust(2),
    updated_readme
)

# Write the updated content back to README
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(updated_readme)

print("✅ README updated successfully!")
