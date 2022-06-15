def count_char(password):
    i = 0
    for letter in password:
        i += 1
    return i

def check_if_no_space(password):
        if ' ' in password:
            return False
        return True

def check_if_maj(password):
    upper = False
    for letter in password:
        if letter.isupper():
            upper = True
    return upper

def check_if_special(password):
    result = False
    special = ['!', '*', '-']
    for letter in password:
        if letter in special:
            result = True
    return result

def check_if_valid_password(password):
    password_len_max = 10
    password_len_min = 5
    if count_char(password) < password_len_min:
        return False
    if count_char(password) > password_len_max:
        return False
    if check_if_no_space(password) == False:
        return False
    if check_if_maj(password) == False:
        return False
    if check_if_special(password) == False:
        return False
    return True

result = check_if_valid_password("Bonj!ou")
if result == True:
    print("password is valid")
else:
    print('password is invalid')