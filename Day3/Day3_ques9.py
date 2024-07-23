#find the elements present in k+ith index
#1.sample i/p-->k=3 
# n=2 
# array elements are 3 6 8 4 61 2
#o/p=2
#-----------------------#
#2.sample input 
# k=3 
# n=4 
# input=70 54 36 72 
# output=error
#-----------------------#
k=int(input())
n=int(input())
l=list(map(int,input().split()))
sum=0
if (len(l)<k+n):
    print("error")
else:
    for i in range(len(l)):
        sum=k+n
        print(l[sum])
        exit(0)