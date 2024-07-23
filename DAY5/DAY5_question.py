#check whether how many vowels in string
'''n=input()
count=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in n:
    if i in vowels:
        count+=1
print(count)'''

#gives wrong output
'''n=input()
n1=(n.lower())
vowel=0
consonant=0
vowels=['a','e','i','o','u']
consonants="bcdfghjklmnpqrstvwxyz"
for i in n1:
    if i in vowels:
        vowel+=1
    elif i in consonants:
        consonant+=1
print(consonant)
print(vowel)'''

#write a program to print all the vowels followed by consonants
'''n=input()
n1=(n.lower())
x=""
vowel=0
vowels=['a','e','i','o','u']
consonants="bcdfghjklmnpqrstvwxyz"
for i in n1:
    if i in consonants:
        x+=i
print(x)'''

#print the non repeating characters in a string/unique elements
'''n=input()
res=""
count=0
for i in n:
    if i not in res:
            res+=i
print(res)'''

#input=hello world 123
'''n=input()
digits='0123456789'
res=0
for i in n:
    if i in digits:
        res+=int(i)
print(res)'''

#reverse of string       *****practice******
'''str=input()
n=int("1234")
temp=0
while n!=0:
    x=n%10
    temp+=x'''
