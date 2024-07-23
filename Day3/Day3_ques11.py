#find the max element in a given list
#1.Test case 
# Input:12 23 36 44 45 57 
# output=57
'''l=list(map(int,input().split()))
print(*l)
print(max(l))'''
#OR
'''l=list(map(int,input().split()))
max=0
for i in range(0,len(l)):
    for j in range(1,len(l)):
        if(l[i]<l[j]):      
            max=l[j]
print(max)'''
#OR
'''l=list(map(int,input().split()))
max=0
for i in range(len(l)):
    if(l[i]>max):
        max=l[i]
print(max)'''


#minimum element
'''l=list(map(int,input().split()))
min=l[0]
for i in range(len(l)):
    if(l[i]<min):
        min=l[i]
print(min)'''

#replace the elements in the array with avg of max and min element
'''l=list(map(int,input().split()))
min=l[0]
for i in range(len(l)):
    if(l[i]<min):
        min=l[i]
print(min)
max=l[0]
for i in range(len(l)):
    if(l[i]>max):
        max=l[i]
print(max)
avg=(max+min)//2
for i in range(len(l)):
    l[i]=avg
print(l)'''

#find missing of a number
#Logic--->sum of n natural numbers-sum of elements in an array
'''l=list(map(int,input().split()))
n=int(input())
x=(n*(n+1))//2
sum=0
for i in range(len(l)):
    sum+=l[i]
    z=x-sum
print("missing number is",z)'''

#Find the array with no duplicates
'''l=list(map(int,input().split()))
no_duplicates=[]
for i in l:
    if (i not in no_duplicates):
        no_duplicates.append(i)
print(*no_duplicates)'''

#find the duplicates in array
'''l=list(map(int,input().split()))
duplicates=[]
for i in l:
    if (i not in duplicates):
        duplicates.append(i)
    print(duplicates)'''

#adding a number input-->123 output-->1+2+3=6
'''n=int(input())
sum=0
while n!=0:
    x=n%10
    sum+=x
    n=n//10
print("sum is",sum)'''

#Find the sum of squares of a digit in a given
'''n=int(input())
sum=0
while n!=0:
    x=n%10
    sum+=x**2
    n=n//10
print("square of a given number is",sum)'''

#find sum of even digits in even number
'''n=int(input())
sum=0
while n!=0:
    x=n%10
    if(x%2==0):
        sum+=x
    n=n//10
print("sum is",sum)'''

#reverse a number
n=int(input())
reverse=[]
rev=0
r=""
while n!=0:
    x=n%10
    reverse.append(x)#OR
    rev=rev*10+x#OR
    r=r+str(x)
    n=n//10
print(*reverse)
print(rev)
print(int(r))