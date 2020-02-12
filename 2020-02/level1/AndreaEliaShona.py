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
        if letter in str(digits):
            score = score + 5
            break

    if ' ' in password:
        score = score + 5

    #for letter in password:
    #    if (letter.isspace()) == True:
    #        score = score + 5
    #        break
    
    for letter in password:
        if letter not in lowercase + uppercase + str(digits) + " ":
            score = score + 10
            break
 
    # to be finished
    # if username.lower in password:
    #     score = score - 15
            
            
    
    return score
