# We'll find a phone number without a regualr expression
# Number format is 123-456-7890

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal(): # check if the first three characters are numbers
            return False
    if text[3] != '-': # check if the fourth character is a dash
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


# Test the function
'''
print('415-555-1234 is a phone number:')
print(isPhoneNumber('415-555-1234'))

print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))
'''

# Further Improvement

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

def retrivePhoneNumber(message):
    for i in range(len(message)):
        piece = message[i : i+12]
        if isPhoneNumber(piece):
            print('Phone number found: ' + piece)
    print('Done')

retrivePhoneNumber(message)
