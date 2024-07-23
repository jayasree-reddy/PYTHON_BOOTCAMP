#PASSWORD VERIFIER
#mr.x is trying to create a new password for his instagram account these are the 
#required conditions for creating a new password
#condition 1:minimum length is 8 and maximum length is 15
#condition 2:only @,/ is allowed in a password
#condition 3:no spaces are allowed
#condition 4:only alpha numerics are allowed
#you are supposed to print weak password if length is exact 8
#medium password if length is b/w 8-12
#strong password if length is b/w 12-15
password=input()
length=len(password)
str="@/"
count=0
if (length>=8 and length<=15):
    for i in password:
        if i in str[0] or str[1]:
            for i in password:
                if i!=" ":
                    count+=1
    print("acc")
else:
    print("not acc")
if(length==8):
    print("weak password")
elif(length>8 and length<12):
    print("medium length")
else:
    print("strong")