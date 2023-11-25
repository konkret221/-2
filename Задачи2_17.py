def hacker_encode(input_string):
    encoded_string = ""
    for char in input_string:
        if char.lower() == 'а':
            encoded_string += '4'
        elif char.lower() == 'е':
            encoded_string += '3'
        elif char.lower() == 'о':
            encoded_string += '0'
        else:
            encoded_string += char
    return encoded_string

text = "Вечер в хату"
encoded_text = hacker_encode(text)
print(encoded_text)