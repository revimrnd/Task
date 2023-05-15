import random

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIAL = '~!@#$%^&*()_+'
length = 8
join = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
join_results = [random.choice(join) for _ in range(length)]
password = ''.join(join_results)

for char in password:
    if char in LOWER_LETTERS:
        hasLowerCase = True
    if char in UPPER_LETTERS:
        hasUpperCase = True
    if char in NUMBERS:
        hasNumber = True
    if char in SPECIAL:
        hasSpecial = True

print(password)