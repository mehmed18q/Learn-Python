# Refrences

import string
import random
# My Code


def GeneratePassword(passLength):
    password = string.ascii_letters + string.digits + "!@#$%^&*()_+|?><"
    passwordList = []
    for passChar in range(passLength):
        passRandom = random.choice(password)
        passwordList.append(passRandom)
    finalPassword = "".join(passwordList)
    return finalPassword
