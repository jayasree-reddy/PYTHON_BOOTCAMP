#strings are immutable
#The methods are len,isUpper,isLower,toUpper,toLower,concat(+),isAlpha,isDigit,isAlnum,titleCase,swapCase
'''s=input()
print(len(s))
print(s.isupper())
print(s.islower())
print(s.isalpha())#without space
print(s.isnumeric())#everthing should be numeric
print(s.isalnum())#without space returns True
print(s.isascii())#whether the given number is ascii or not
print(s.isdigit())
print(s.title())#gives first letter of a word with capital
print(s.upper())
print(s.lower())
print(s.isspace())
print(s.swapcase())
print(s.replace('h','#'))
print(s.split())
print(s.split('o'))
print(s.strip())#trims the space which is at the beginning and ending of input
s1="hello"
concat=s+s1
print(concat)'''

#------>Character to ASCII<--------#
print(ord('a'))
print(ord('A'))
print(ord('0'))
print(ord('('))

#------->ASCII to Character<---------#
print(chr(65))