import re


def isPhoneNumber(phoneNum):
    phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

    # Check if the phone number matches the regex pattern
    if phoneNumRegex.match(phoneNum):
        return True
    else:
        return False
    

def serachPhoneNumber(message, show_numbers=True):
    number_of_numbers = 0
    for i in range(len(message)):
        if i + 12 <= len(message):
            piece = message[i : i+12]
            if isPhoneNumber(piece):
                number_of_numbers += 1
                i += 12
                if show_numbers:
                    print('Phone number found: ' + piece)
        
        else:
            continue
    print('Done')
    print("Total numbers found: " + str(number_of_numbers))
