#=====================================Some=Basic=Functions==============================================================

def isSymbol(char):
    symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?','@', '[', '\ ', ']', ' ^ ', '_', '`', '~']
    if char in symbols:
        return True
    else:
        return False
def isNumber(char):
    try:
        int(char)
    except ValueError:
        return False
    else:
        return True
def isUppercase(char):
    for i in range(65,91):
        if char == chr(i):
            return True
    return False
def isLowercase(char):
    for i in range(97,123):
        if char == chr(i):
            return True
    else:
        return False

#===================================================The=Main=Function===================================================

def check_password_strength(string):
    if len(string)==0:
        return 0 # just in case nothing is introduced
    elif len(string)<5 :
        return 0 # a less than 5 characters password is a weak password
    points=0
    if len(string)<8:
        points-=1
    if len(string)>12:
        points+=1
    atLeastAnUppercase = False
    atLeastALowercase = False
    atLeastASymbol = False
    numberCounter=0
    consecutiveNumbers=0
    for i in range(len(string)):
        if isSymbol(string[i]) and not atLeastASymbol:
            atLeastASymbol=True
            points+=1
        if isNumber(string[i]):
            numberCounter+=1
            if i > 0 and isNumber(string[i-1]):
                if int(string[i]) == int(string[i-1])-1 or int(string[i]) == int(string[i-1])+1 or int(string[i])==int(string[i]):
                    consecutiveNumbers += 1 # if we get pairs of consecutive numbers like '1234' or '5432' then we will increase consecutiveNumbers
        if isUppercase(string[i]) and not atLeastAnUppercase:
            atLeastAnUppercase = True
            points+=1
        if isLowercase(string[i]) and not atLeastALowercase:
            atLeastALowercase = True
            points+=1
    if consecutiveNumbers != numberCounter-1 : # then not all the numbers are consecutives so we will give a point for that, also i set numberCounter-1 because we wil not count the first number in the consecutiveNumbers
        points+=1
    if points<0: # we will get here only when we will have the same
        points=0
    return points

def interpret_results(int):
    if int == 0 :
        print("[{}]".format(int),"very weak password.\nMaybe the password is too short also add at least a lowercase and  an uppercase letter")
    elif int == 1:
        print("[{}]".format(int),"weak password.\nTry to add lowercase and uppercase letters.")
    elif int == 2:
        print("[{}]".format(int),"Better password.\nTry to add some numbers and maybe a symbol or two.")
    elif int == 3:
        print("[{}]".format(int),"Good password.\nHave you tried to not use consecutive numbers?")
    elif int == 4:
        print("[{}]".format(int),"Strong password.\nThat's a very good password but also you can improve it.")
    elif int == 5:
        print("[{}]".format(int),"Very Strong password.\nWell i think your password is secure enough to use it, have fun keeping your data safe :) ")

#========================================================Application====================================================
password=input("Introduce your password:\n")
interpret_results(check_password_strength(password))
res=input("\nType anything to close the program.")