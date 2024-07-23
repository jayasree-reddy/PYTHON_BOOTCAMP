#print even or odd
'''n=int(input())
if n%2==0:
    print("even number")
else:
    print("odd number")'''

#find greatest of 3
'''a,b,c=map(int,input().split())
if (a>b and a>c):
    print("a is greatest")
elif(b>c):
    print("b is greater")
else:
    print("c is greater")'''

#find sum of all elements in an array
'''l=list(map(int,input().split()))
sum=0
for i in l:
    sum+=i
print(sum)'''

#*****find peak element in an array
l=list(map(int,input().split()))
count=0
for i in range(1,len(l)-1):
    if l[i]>(l[i-1]) and l[i]>(l[i+1]):
        count=i #first peak element
if l[-1]>l[-2] and l[-1]>count:
        count=len(l)-1#last peak element
        #print(l[i],end=" ")
print(l[count])#first peak element

#find max element in an array
'''l=list(map(int,input().split()))
max=0
for i in l:
    if(i>max):
        max=i
print(max)'''

#find second max element in an array
'''l=list(map(int,input().split()))
max=0
for i in l:
    if(i>max):
        max=i
print(max)
sec_max=0
for j in l:
    if(j>sec_max and j!=max):
        sec_max=j
print("second maximum element is",sec_max)'''

#reverse an array without using built in functions
'''l=list(map(int,input().split()))
print(*l[::-1])'''

#find the sum of squares of given number
'''n=int(input())
sum=0
while n>0:
    x=n%10
    sum+=x**2
    n=n//10
print(sum)'''

#find sum of squares of even and odd digits
'''n=int(input())
odd_Squaresum=0
even_Squaresum=0
while n>0:
    x=n%10
    if(n%2==0):
        even_Squaresum+=x**2
    else:
        odd_Squaresum+=x**2
    n=n//10
print(even_Squaresum)
print(odd_Squaresum)'''

#check whether given number is palindrome or not using while loop
'''n=int(input())
temp=n
rev=""
while n>0:
    x=n%10
    rev+=str(x)
    n=n//10
print(rev)
if(int(rev)==temp):
    print("Given number is a palindrome")
else:
    print("not a palindrome")'''

#write a program to print first n fibinocci series
'''n=int(input())
a=0
b=1
for i in range(n):
    temp=a+b
    a=b
    b=temp
print("fibinocci series",temp)'''

#To swap a and b without 3rd variable
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)'''

#sum of natural numbers
'''n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)'''