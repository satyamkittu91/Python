import re

import re._compiler

def isPhoneNumber(text):
    phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    mo = phoneNumRegex.search(text)
    return mo


# Grouping with parentheses

def isPhoneNumber(text):
    phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
    mo = phoneNumRegex.search(text)
    return mo.group(1), mo.group(2), mo.group(3) 

'''
for 415-555-4242
isPhoneNumber('415-555-4242')
('415', '555', '4242')
'''

# Matching multiple groups with the Pipe (| Character)

villainReg = re.compile(r'Batman| Superman')
mo1 = villainReg.search('Batman and Superman')
print(mo1.group(0)) # Batman

mo2 = villainReg.search('Superman and Batman')
print(mo2.group(0)) # Superman


    # matching one of the serveral patterns
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group()) # Batmobile
print(mo.group(1)) # mobile


print("Optional matching with the question mark (?)")

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group()) # Batman

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group()) # Batwoman

print("Matching zero or more with the star (*)")

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group()) #Batman

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group()) #Batwoman

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group()) #Batwowowowoman


print("Matching one or more with the Plus (+)")

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group()) # Batwoman

mo2 = batRegex.search("The Adventure of Batwowowowoman")
mo2.group()
print(mo2.group()) # Batwowowowoman

mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None) # True

print("Matching specific Repetitions with curly Brackets ({})")

batRegex = re.compile(r'Bat(wo){2,4}man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1 == None) # True

mo2 = batRegex.search('The Adventures of Batwowowoman')
print(mo2.group()) # Batwowowoman



print("Greedy and Non-Greedy Matching")
# Python automatically makes the regex engine greedy, meaning it will try to match as much text as possible.
# To make it non-greedy, add a question mark after the curly brackets.

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group()) # HaHaHaHaHa

nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group()) # HaHaHa


print("\nThe findall() method")
# The findall() method returns a list of all matches in the string.
# If the regex has groups, it returns a list of tuples.
# the search only returns the first match.
# The findall() method returns all matches in a list.

phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo) # [('415', '555', '9999'), ('212', '555', '0000')]
print(mo[0]) # ('415', '555', '9999')
print(mo[0][0]) # 415


# The Carent (^) and the Dollar sign ($)
# The caret (^) matches the beginning of a string.
# The dollar sign ($) matches the end of a string.
# The regex ^Hello will match any string that starts with Hello.
# The regex world$ will match any string that ends with world.
# The regex ^Hello world$ will match the string Hello world exactly.


# The wildcard Character (.)
# The dot (.) matches any character except a newline.
# The regex .at will match any string that has at in it, such as cat, hat, bat, etc.

atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the mat.')
print(mo) # ['cat', 'hat', 'sat', 'mat']


# Matching everything with Dot Star (.*)
# The dot star (.*) matches everything except a newline.
# The regex .* will match any string, including an empty string.
# The regex .*? will match any string, including an empty string, but it will be non-greedy.
# The regex .* will match everything in the string, including newlines.

# Matching Newlines with the Dot Character
noNewlineRegex = re.compile(r'.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
# Serve the public trust.

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
# Serve the public trust. \nProtect the innocent. \nUphold the law.

'''
The ? matches zero or one of the preceding group.
• The * matches zero or more of the preceding group. 
• The + matches one or more of the preceding group. 
• The {n} matches exactly n of the preceding group. 
• The {n,} matches n or more of the preceding group.
• The {,m} matches 0 to m of the preceding group.
• The {n,m} matches at least n and at most m of the preceding group.
• {n,m}? or *? or +? performs a nongreedy match of the preceding group.
• ^spam means the string must begin with spam.
• spam$ means the string must end with spam.
• The . matches any character, except newline characters.
• \d, \w, and \s match a digit, word, or space character, respectively.
• \D, \W, and \S match anything except a digit, word, or space character, respectively.
• [abc] matches any character between the brackets (such as a, b, or c).
• [^abc] matches any character that isn’t between the brackets.
'''


# Case Insensitive Matching
robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
# RoboCop
# re.I makes the regex case insensitive.

# Substituting Strings with the sub() method
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# CENSORED gave the secret documents to CENSORED.

# Use the matched text itself as the part of the substitution.
# The sub() method takes a function as the second argument.
# The function takes a match object as the argument and returns the string to be used as the replacement.
agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice gave the secret documents to Agent Bob.')
# A**** gave the secret documents to B****.


# Verbose mode
# The verbose mode allows you to write regexes that look nice and readable.
# You can add comments and whitespace to the regex.
phoneRegex = re.compile(r'''(
    (\d{3}|\(d{3}\))? # area code
    (\s|-|\.)? # separator
    (\d{3}) # first three digits
    (\s|-|\.) # separator
    (\d{4}) # last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
    )''', re.VERBOSE)


# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
# You can combine the flags by using the bitwise OR operator (|).
# For example, re.IGNORECASE | re.DOTALL | re.VERBOSE will make the regex case insensitive, match newlines, and be verbose.

someRegexValue = re.compile(r'some regex', re.IGNORECASE | re.DOTALL | re.VERBOSE)