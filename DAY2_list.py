'''list
Aggregate functions-->min,sum,avg
list-->Ordered
'''
#creating a list
list=[1,2,3,4,-12,-9,7,0]
print(list)
print(*list, end="@")
#append(88)-->adds a value at a  last of a list
list.append(88)
#insert-->we can insert in particular indeex
list.insert(0,999)
print(*list)
#length fun-->returns a length of a list
print(len(list))
#pop-->removes element from list
list.pop()#removes last element
list.pop(2)
print(*list)
#concat of 2 lists-->combines another list at end of the list
list1=[7,8,9]
new_list=list+list1
print(*new_list)
#copy-->it doesn't effect the original list and copies to new list
new_list1=list.copy()
new_list1.pop()
print(*new_list1)
#count-->returns how many times a num is repeated in list
cnt=list.count(2)
print(cnt)
#sort-->it uses quick sort-->time complexity(nlogn)
print(list.sort)#it gives none bez it will return an obj but internally  it can be sorted 
list.sort()
print(*list)#returns a sorted list

print("***Dynamically taking input from the user***")
list=list(map(int,input().split(" ")))#integer
print(*list)

list=list(map(str,input().split()))#string
print(*list)
#list.append(bubbly)-->will not work
list.pop(1)
print(len(list))
#print(count(hi))-->will not work
print(*list)

#PROBLEM 1.append 2.pop 3.sort 4.print len
l1=list(map(int,input().split()))
print("enter the i/p")
print("1.append\n 2.pop\n 3.sort\n 4.print length")
choice=int(input())
if choice==1:
    l1.append(int(input()))
    print(l1)          
elif choice==2:
    l1.pop(int(input()))
    print(l1)
elif choice==3:
    l1.sort()
    print(l1)
elif choice==4:
    print(len(l1))
else:
    print("invlid choice")