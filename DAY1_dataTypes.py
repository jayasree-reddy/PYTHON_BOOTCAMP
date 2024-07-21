#python: Is a programming,Interpreted,high level,object oriented Language
#Data Types: int,float,string,boolean,sets,tuple,dictionary
#dataType:It is called as camelCase It is good for readability
#print("Hello SWEC")
#printing formats---
# 1.printing:
print("Hello")
#to print hello,your name and to use in code further
var_1="python"
print("Good morning",var_1)
#There are 2 types of inputs static and dynamic to take input dynamically:
name=input("enter name\n")
age=input("enter age")
print("hello",name)
#fstring-Formated string
print(f"hello {name} you are {age}yrs old")
#to print marks and its avg
s1=input("enter input")
s2=input()
s3=input()
print(f"your marks are{s1+s2+s3} and average is{(s1+s2+s3)/3}")
#conditional statements--->checks conditions and enters into loop-->if,elif,else
age=int(input())
if age<18:
    print(f"hello {name} you are{age}yrs old not eligible for voting")
elif:
    print(f"hello {name} you are{age}yrs old eligible for voting")
else:
    print(f"hello {name} you are{age}yrs old eligible for voting")