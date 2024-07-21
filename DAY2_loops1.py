l=list(map(int,input().split()))
for i in range(len(l)):
    print(l[i])

#string input
s=input()
for i in s:
    print(i)
for i in range(len(s)):
    print(s[i])

#1.using for loop 1-100
n=100
for i in range(1,n+1):
    print(i)

#2.append 1,100 num in empty list
list=[]
n=100
for i in range(1,n+1):
    list.append(i)
print(*list)

#3.find sum of all using list
l1=list(map(int,input().split()))
sum=0
for i in l1:
    sum+=i
print(sum)