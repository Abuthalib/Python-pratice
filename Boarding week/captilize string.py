def capitalize_string(input_string):
    capitalized = " "
    for char in input_string:
        if char.isalpha():
            if char == char.lower():
                capitalized += chr(ord(char)-32)
            else:
                capitalized += char
        else:
            capitalized += char
    return  capitalized



# Example usage
original_string = "Hello WorLd !! how are you?"
capitalized_result = capitalize_string(original_string)

print("Original String:", original_string)
print("Capitalized String:", capitalized_result)
