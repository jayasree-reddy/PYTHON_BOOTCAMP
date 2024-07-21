#7. you are given with a comma seperated natural numbers 1-10 print only even numbers
l=list(map(int,input().split(",")))
for i in range(1,len(l),1):
    if(i%2==0):
        print(i)

#number of even numbers in list
l=list(map(int,input().split(",")))
count=0
for i in range(1,len(l)+1,1):
    if(i%2==0):
        count+=1
print(count)
#OR
l=list(map(int,input().split(",")))
count=0
for i in range(0,len(l),2):
    count+=1
print(count)
#you are given a space seperated integer list find no.of even and odd in a given list
print("***EVEN'S AND ODD'S***")
l=list(map(int,input().split(",")))
E_count=0
O_count=0
for i in range(len(l)):
    if(l[i]%2==0):
        E_count+=1
    else:
        O_count+=1
print("even count=",E_count,"Odd count=",O_count)