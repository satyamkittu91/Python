import json

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Max", 27)

def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    
    else:
        raise TypeError("Object of type User is not JSON serializable")

from json import JSONEncoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

user_json = json.dumps(user, default=encode_user)
user_json1 = json.dumps(user, cls=UserEncoder)
user_json2 = UserEncoder().encode(user)
print(user_json) # Output: {"name": "Max", "age": 27, "User": true}
print(user_json1) # Output: {"name": "Max", "age": 27, "User": true}    

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct

user = json.loads(user_json, object_hook=decode_user)
print(type(user)) # Output: <class '__main__.User'>
print(user.name) # Output: Max
print(user.age) # Output: 27