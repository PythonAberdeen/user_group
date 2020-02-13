def rate_password(username, password):
    lc = uc = num = spc = oth = usn = 0
    
    for n in password:
        if n.islower(): lc = 2
        if n.isupper(): uc = 3
        if n.isdigit(): num = 5 
        if n.isspace(): spc = 5
        if not n.isalnum():  oth = 10
    if password.find(username)> -1: usn = -15
        
    score = len(password) + lc + uc + num + spc + oth + usn
    if score < 0: score = 0
        
    return score
