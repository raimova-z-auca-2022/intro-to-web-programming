import os
import csv
import json

# 1. Writing to a Text File
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Python makes file handling easy.\n")

# 2. Reading from a Text File
with open("example.txt", "r") as file:
    content = file.read()
    print("Text File Content:")
    print(content)

# 3. Reading Line by Line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# 4. Appending to a File
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")

# 5. Checking if File Exists
if not os.path.exists("newfile.txt"):
    with open("newfile.txt", "x") as file:
        file.write("This is a new file.\n")

# 6. Writing to a CSV File
with open("data.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age", "City"])
    writer.writerows([
        ["Alice", 25, "New York"],
        ["Bob", 30, "Los Angeles"],
        ["Charlie", 22, "Chicago"]
    ])

# 7. Reading from a CSV File
with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    print("\nCSV File Content:")
    for row in reader:
        print(row)

# 8. Reading CSV with Headers
with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    print("\nCSV with Headers:")
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']}")

# 9. Writing to a JSON File
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

# 10. Reading from a JSON File
with open("data.json", "r") as json_file:
    data = json.load(json_file)
print("\nJSON File Content:")
print(data)

# 11. Converting JSON to Python Dictionary
json_string = '{"name": "Alice", "age": 25, "city": "New York"}'
python_dict = json.loads(json_string)
print("\nJSON to Python Dictionary:")
print(python_dict)

# 12. Converting Python Dictionary to JSON
python_dict = {"name": "Bob", "age": 30, "city": "Los Angeles"}
json_string = json.dumps(python_dict, indent=4)
print("\nPython Dictionary to JSON:")
print(json_string)