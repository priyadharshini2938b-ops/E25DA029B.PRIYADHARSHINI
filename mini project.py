import re
def password_checker(password):
    length = re.search(r".{8,}", password)
    upper = re.search(r"[A-Z]", password)
    lower= re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    score = 0
    if length: score += 1
    if upper: score += 1
    if lower: score += 1
    if digit: score += 1
    if special: score += 1
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Better"
    else:
        return "Weak"
password = input("Enter a password: ")
print(password_checker(password))
