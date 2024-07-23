#print the element in a particular index CYCLIC PRINTING
#1.sample input
#k=18 
# input=3 6 8 4 61  
# output=3(index)
#2.sample input 
# k=8 
# input=80 70 54 36 72 
# output=36            
k=int(input())
l=list(map(int,input().split()))
index=k%len(l)
print(l[index-1])
print(index)