'''for i in range(32,128):
    print(chr(i),end=" ")'''

#print the sum of digits using ASCII values
'''n=input()
sum=0
for i in n:
    if ord(i)>=48 and ord(i)<=57:
        sum+=int(i)
print(sum)'''

#write  a program to print all the capital letters in given string
'''n=input()
s=""
for i in n:
    if ord(i)>=65 and ord(i)<=96:
        s+=i
print(s)'''

#remove all the braces from string
'''n=input()
x='()[]{}'
str=""
for i in n:
    if i not in x:
        str+=i
print(str)'''

#method 2
'''n=input()
for i in n:
    if ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==125 or ord(i)==127:
        pass
    else:
        print(i,end=" ")'''

#print the character after 4 letter *****PRACTICE*********
'''n=input()
for i in n:
    x=ord(i)+4
    y=chr(x)
    print(y,end="")'''

#input:hello---wor--ld 
# output:-----helloworld
'''n=input()
res=""
count=0
for i in n:
    if i=='-':
        count+=1
print(count)
for i in n:
    if ord(i)>=97 and ord(i)<=123:
        res+=i
print('-'*count+res)'''

#method 2
'''n=input()
res=""
count=0
for i in n:
    if i=='-':
        count+=1
    else:
        res+=i
print('-'*count+res)'''