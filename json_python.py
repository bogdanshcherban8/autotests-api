import json
json_data = """{
  "name": "Bob",
  "age": 20,
  "is_student": false,
  "courses": [
    "Python",
    "Qa Automation",
    "API Testing"
  ],
  "address": {
    "city": "Moscow",
    "zip": "1234321"
  }
}
"""
parsed_data= json.loads(json_data)
print(parsed_data['courses'])

data = {"name": "Alice",
  "age": 25,
  "is_student": True}

json_string = json.dumps(data, indent=4)
print(json_string)

with open("json_example.json", "r", encoding="utf-8") as file:
    read = json.load(file)
    print(read)

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

with open("json_big.json", "w", encoding="utf-8") as file:
    json.dump(parsed_data, file, indent=4, ensure_ascii=False)