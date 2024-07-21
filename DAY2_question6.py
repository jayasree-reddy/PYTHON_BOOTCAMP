#take a space seperated i/p from user and print alternate elements
l=list(map(int,input().split()))
print(*l[0::2])
for i in range(0,len(l),2):
    print(l[i],end=" ")