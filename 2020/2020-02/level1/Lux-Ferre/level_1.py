import re

def main():
    input_pass = input("Type password: ")
    output = rate_password('username',input_pass)
    print(output)

def rate_password(username, password):
    score = 0
    score = score + len(password)
    if username.lower() in password.lower():
        score -= 15
    if contains_lower(password):
        score += 2
    if contains_upper(password):
        score += 3
    if contains_digit(password):
        score += 5
    if contains_space(password):
        score += 5
    if contains_other(password):
        score += 10
    if score < 0:
        score = 0

    return score

def contains_lower(password):
    if re.search("[a-z]+", password):
        return True

def contains_upper(password):
    if re.search("[A-Z]+", password):
        return True

def contains_digit(password):
    if re.search("[0-9]+", password):
        return True

def contains_space(password):
    if re.search("[ ]+", password):
        return True

def contains_other(password):
    if re.search("[^a-zA-Z0-9 ]+", password):
        return True

if __name__ == '__main__':
    main()