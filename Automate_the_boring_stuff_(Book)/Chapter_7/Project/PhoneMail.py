import re, pyperclip

# Define phone regex pattern
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # area code
    (\s|-|\.)?              # separator
    (\d{3})                 # first three digits
    (\s|-|\.)               # separator
    (\d{4})                 # last four digits
    (\s*(ext|x|ext\.)\s*(\d{2,5}))? # extension
    )''', re.VERBOSE)

# Define email regex pattern
emailRegex = re.compile(r'''
    [a-zA-Z0-9._%+-]+   # local part
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    \.[a-zA-Z]{2,}      # top-level domain
''', re.VERBOSE)

# Get text from clipboard
text = str(pyperclip.paste())

# Check if clipboard has text
if not text.strip():
    print("Clipboard is empty or does not contain text.")
    exit()

matches = []

# Find all phone numbers
for groups in phoneRegex.findall(text):
    if groups[1] != '':
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    else:
        phoneNum = '-'.join([groups[3], groups[5]])

    # extension
    if groups[8]:
        phoneNum += ' x' + groups[8]
    
    matches.append(phoneNum)

#Find all emails
for match in emailRegex.findall(text):
    matches.append(match)


# copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
# print the results


'''
Other Similar ideas
- Find website URLs that begin with http:// or https://
- Find dates in the format YYYY-MM-DD or MM/DD/YYYY
- Remove sensitive information from text (e.g., credit card numbers, social security numbers)
- Validate and format phone numbers
- Fidn common typos such as multiple spaces between words, accidentally repeated words, or multiple
    exclamation marks
'''