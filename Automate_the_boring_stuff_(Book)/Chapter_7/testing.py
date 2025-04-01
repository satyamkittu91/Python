import random
from without_re import retrivePhoneNumber
# We'll find a phone number without a regualr expression

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdigit():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdigit():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdigit():
            return False
    return True

def test_phone_number_search(message):
    for i in range(len(message)):
        piece = message[i : i+12]
        if isPhoneNumber(piece):
            print('Phone number found: ' + piece)
    print('Done')

def generate_long_string(length):
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ- "
    return ''.join(random.choice(characters) for i in range(length))

def generate_phone_numbers(num_phones):
    phone_numbers = []
    for _ in range(num_phones):
        area_code = ''.join(random.choice('0123456789') for _ in range(3))
        prefix = ''.join(random.choice('0123456789') for _ in range(3))
        line_number = ''.join(random.choice('0123456789') for _ in range(4))
        phone_numbers.append(f"{area_code}-{prefix}-{line_number}")
    return phone_numbers

def create_super_long_string_with_phones(length, num_phones):
    phone_numbers = generate_phone_numbers(num_phones)
    long_string = generate_long_string(length)
    
    phone_positions = random.sample(range(length - 12), min(num_phones, length - 12))
    
    long_string_list = list(long_string)

    for i, pos in enumerate(phone_positions):
        for j, char in enumerate(phone_numbers[i]):
            if pos + j < len(long_string_list):
                long_string_list[pos + j] = char

    return "".join(long_string_list)


# Generate a long string:
long_string = create_super_long_string_with_phones(1000000, 20000) #1 million characters, 2000 phone numbers.

# Print the string (you can copy and paste this into your test):
retrivePhoneNumber(long_string, show_numbers=False)