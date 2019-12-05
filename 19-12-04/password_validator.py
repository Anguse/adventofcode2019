import string

def valid_password(password):
    duplicates = []
    duplicate = 0
    valid = True
    for i in range(len(password)-1):
        if password[i+1] < password[i]:
            valid = False
        if password[i+1] == password[i]:
            duplicate += 1
        else:
            duplicates.append(duplicate)
            duplicate = 0
    duplicates.append(duplicate)

    if not 1 in duplicates:
        valid = False
    return valid
        
if __name__ == '__main__':
    valid_pws = 0
    for i in range(172851, 675869):
        if valid_password(str(i)):
            valid_pws += 1
    print(valid_pws)
    
    
