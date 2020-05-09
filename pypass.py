# Generate a random password. 
import secrets

x         = 0
password  = ""
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # Len == 26 secrets.randbelow(26)
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # Len == 26 secrets.randbelow(26)
numbers   = ['0','1','2','3','4','5','6','7','8','9','10'] # Len == 11 secrets.randbelow(11)
symbols   = ['*','%','#','@','!','&','^','$'] # Len == 8 secrets.randbelow(8)

try:
    passLength = int(input('Please enter the desired password length (max: 256): '))
except: 
    print ('[-] Enter an integer.')
    exit()
if passLength > 256: 
    print ('[-] The script was pretty clear as to the length of the password.')
    exit()
elif passLength == 0:
    print ('[-] No.')
    exit()
elif passLength < 12:
    print ('[-] Do you want this account to be secure?')
    exit()
else: 
    pass

print ('[+] Generating a {0} character password'.format(passLength))

def generateUpper():
    zulu = uppercase[secrets.randbelow(26)]
    return zulu

def generateLower():
    yankee = lowercase[secrets.randbelow(26)]
    return yankee

def generateNumber():
    xray = numbers[secrets.randbelow(11)]
    return xray

def generateSymbol():
    mike = symbols[secrets.randbelow(8)]
    return mike

while x < passLength:
    alpha = secrets.randbelow(4)
    if alpha == 0:
        password += generateUpper()
    elif alpha == 1: 
        password += generateLower()
    elif alpha == 2:
        password += generateNumber()
    elif alpha == 3:
        password += generateSymbol()
    else:
        print ('[-] How.')
        exit()
    x += 1

print ('[+] Here is your shiny new password: ' + password)