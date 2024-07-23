#*********PRIME NUMBER**********
#without importing math function
'''n=int(input())
fact=0
if n==1:
    print("not a prime")
for i in range(2,int(n**(0.5))+1):
    if(n%i==0):
        fact+=1
        break
if fact==0:
    print("prime number")
else:
    print("not a prime")'''

#write aa program to print all prime num in given range
'''n=int(input())
m=int(input())
fact=0
if n==1:
    print("not a prime")
for i in range(n,m+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i,end=" ")'''

#********LEAP YEAR*********
'''year=int(input())
if year%400==0:
    print("leap year")
elif(year%4==0 and year%100!=0):
        print("leap year")
else:
    print("not a leap year")'''

#by for loop LEAP YEAR
year=int(input())
year1=int(input())
count=0
for i in range(year,year1+1):
    if i%400==0:
        print(i,"is leap year")
    elif(i%4==0 and i%100!=0):
        print(i,"is leap year")
        count+=1
    else:
        print("not a leap year")
print(count)