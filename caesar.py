def alphabet_position(letter):
    posi = ord(letter.lower())
    return posi - 97

def rotate_character(char, rot):
    if not char.isalpha():
        return char
    else:
        posi = alphabet_position(char)
        new_posi = (posi + rot) % 26
        new_char = chr(new_posi + 97)
        if char == char.upper():
            return new_char.upper()
        else:
            return new_char

def encrypt(text, rot):
    lst = list(text)
    new_text = ""
    for char in lst:
        new_char = rotate_character(char, rot)
        new_text += new_char
    return new_text
