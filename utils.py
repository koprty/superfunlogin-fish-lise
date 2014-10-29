d = {}
def authenticate(uname,pword):
    return uname=="Thluffy" and pword=="Clyde"
def adduser(uname,pword):
    if uname not in d:
        d[uname]= pword
        return 1
    else:
        return 0
