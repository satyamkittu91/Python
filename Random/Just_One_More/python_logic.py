

def main():
    entered_string = input("Enter a string: ")
    if not entered_string:
        print("You entered an empty string.")
    else:
        print(f"The first non-repeating character from string {entered_string} is '{first_non_repeating_character(entered_string)}'.")


def first_non_repeating_character(s):
    try:
        s = str(s)
    except:
        raise TypeError("Input must be a string")
    
    for character in s:
        if s.count(character) == 1:
            return character
    
    raise ValueError("No non-repeating character found.")

if __name__ == "__main__":
    main()