import secrets
import random
import string

    #OBTAIN A SET OF ALL CHARACTERS AND DIGITS
allchars = string.ascii_letters+string.digits


while True:
    password = ''.join(secrets.choice(allchars) for i in range(10))
    # CHECKS CONDITIONS THAT NEED TO BE SATISFIED
    if (any(c.islower() for c in password)
        and any(c.isupper() for c in password)
        and sum(c.isdigit() for c in password) >= 2):
        break
print("Here is your randomly generated password:",password)
