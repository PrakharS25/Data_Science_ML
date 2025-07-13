# Write a program to parse and display JSON data from a string.
import json
data = '{"name": "Prakhar", "age": 19}'
parsed = json.loads(data)
print(parsed["name"], parsed["age"])