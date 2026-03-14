import re

def check_password(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)

    score = sum([bool(length), bool(upper), bool(lower), bool(digit)])

    if score == 4:
        print("Strong password")
    elif score >= 2:
        print("Moderate password")
    else:
        print("Weak password")