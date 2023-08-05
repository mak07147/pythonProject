def filter_string(string, char):
    result = ''
    for current_char in string:
        if current_char != char.lower() and current_char != char.upper():
           result = result + current_char
    return result
print(filter_string('If I lOOk forward I am win', 'o'))
