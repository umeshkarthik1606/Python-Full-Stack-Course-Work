
# Password generation
pwd = input ("Enter the Password: ")

if len(pwd)>=8:
    s=set()
    for i in pwd:
        if i.isupper():
            s.add("upper")
        elif i.islower():
            s.add("lower")
        elif i.isdigit():
            s.add("digit")
        else:
            s.add("splchar")
    if len(s)==4:
        print("Strong Password")
    else:
        print("Weak Password : Password must contain uppes case, lower case, digits, special charecters")
else:
    print("Length needs to be >= 8")




