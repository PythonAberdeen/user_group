import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = [0,1,2,3,4,5,6,7,8,9]

def rate_password(username, password):
    score = 0
    score = score + len(password)
    
    for letter in password:
        if letter in lowercase:
            score = score + 2
            break
            
    for letter in password:
        if letter in uppercase:
            score = score + 3
            break

    for letter in password:
        # <error> str(digits) creates whitespaces between values, so "Bob cat 猫" scores +5 because of the space
        # if letter in str(digits): 
        # <fix> added method ".replace(" ", "")" to replace whitespaces with no spaces
        if letter in str(digits).replace(" ", ""): 
            score = score + 5
            break

    if ' ' in password:
        score = score + 5

    for letter in password:
        if letter not in lowercase + uppercase + str(digits) + " ":
            score = score + 10
            break
 
    # <error> this won't penalise "BobX" in "BoB cat 猫" because "if .. in .." checks for the entire username
    # if username.lower() in password.lower():
    # <fix> used method "find()" (it returns the first position of the matched string; otherwise -1)
    # <fix> set both username and password lowercase to avoid case sensitive
    if password.lower().find(username.lower()) > -1:
        score = score - 15            
    
    # set minimum score at 0
    if score >= 0:
        return score
    else:
        return 0
