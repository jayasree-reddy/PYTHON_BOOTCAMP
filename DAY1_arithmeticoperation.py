print("ARITHMETIC OPERATORS")
a=int(input())
b=int(input())
print(f"sum is {a+b} subtract is{a-b} mul is{a*b} div is {a/b}")
#power to print
print(a**b) #or we can import math fun and use pow
#logical operators--> and,or
age=int(input())
if(age>=18 and age<24):
    print("allowed to ride only 2 wheeler")
elif(age>=24 and age<45):
    print("2 wheeler and 4 wheeler")
else:
    print("All")
#problem:
print("************************************")
apples=int(input())
bananas=int(input())
oranges=int(input())
amt_given=700
totalamt=apples*15+bananas*4+oranges*4
remaining_amt=amt_given-totalamt
print(remaining_amt)
if(totalamt>700):
    print("cheated")
else:
    print("not cheated")
print("************************************")
a=int(input())
if(a>0 and a%2==0):
    print("positive and even number")
elif(a>0 and a%2!=0):
    print("positive and odd")
elif(a<0 and a%2==0):
    print("negative and even")
else:
    print("negative and odd number")

#QUESTION:
#mr.z is selected for olympics is participating in swimming competition only 1 winner is
#selected among all participants mr.x and mr.y are frds of z mr.x is participating in 
#batminton and y is participating in table tennins
#acc to selection commette the req for batminton are:
#1.height=140cm 
#2.weight=factors of 2 
#acc to selection committe criteria for table tennins are 
#1.height minimum 118cm to 148cm
#2.weight=no of medals won by mr.z
#according to previous history z participated in 14 games out of which he is having 
#success rate of 50% write a program to check whether mr.x,y,z travel in same 
#plain or not
height_x=int(input())
weight_x=int(input())
height_y=int(input())
weight_y=int(input())
count=0
if(height_x==140 and weight_x%2==0 and height_y in range(118,148) and weight_y%7==0):
    print("Both travels in same plain")
else:
    print("will not travel in same plain")

#PRIME OR NOT by using sqrt(n) method
'''import math
n=int(input())
factor=0
for i in range(2,int(math.sqrt(n)+1),1):
    if(n%i==0):
        factor+=1
        print("not a prime")
        exit(0)
    else:
        print("prime")
        exit(0)
'''
#PRIME OR NOT by using n//2 method
'''n=int(input())
factor=0
for i in range(2,n//2,1):
    if(n%i==0):
        factor+=1
        print("not a prime")
        exit(0)
    else:
        print("prime")
        exit(0)'''
#PALINDROME
print("********PALINDROME*********")
n=int(input())
flag=0
for i in range (1,n):
    if(n[i]==n[i]-1):
        flag+=1
    print("palindrome")
    else:
        flag=0
    print("not a palindrome")