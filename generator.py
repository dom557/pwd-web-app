import random
import string

def generate_password(length=10, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        characters = string.ascii_lowercase  # default to lowercase if no types selected

    password = ''.join(random.choice(characters) for i in range(length))
    return password
