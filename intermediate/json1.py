import json
person = {"name": "Alice", "age": 30, "city": "New York", "hobbies": ["reading", "traveling", "cooking"]}

personJson = json.dumps(person, indent=4, sort_keys=True) # Convert person to JSON string
print(personJson) # Output: {"name": "Alice", "age": 30, "city": "New York", "hobbies": ["reading", "traveling", "cooking"]}

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4) # Write person to person.json file    

with open('person.json', 'r') as file:
    personLoaded = json.load(file) # Load person from person.json file
    print(personLoaded) # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'traveling', 'cooking']}