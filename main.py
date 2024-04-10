# Built-in imports

def reverse(text):
    '''
    Recursive function that reverses a text
    ______________________________________
    text -> str : the text to be reversed
    '''
    if len(text) <= 1:
        return text
    first_char = text[0]
    text = text[1:len(text)]
    text = reverse(text)
    text = text + first_char
    return text


def is_palindrome(string):
    '''
    Recursive Function that takes in a string and check 
    if the string is a palindrome
    _____________________________
    string -> str : the string to be checked
    '''
    string.strip()
    if len(string) <= 1:
        return True
    res = True
    if string[0] == string[-1]:
        res = is_palindrome(string[1:len(string)-1])
    else:
        res = False
    return res
