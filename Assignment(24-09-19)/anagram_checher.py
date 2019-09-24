# -*- coding: utf-8 -*-
str1= input("enter sring 1..>>")
str2= input("enter string 2..>>")
word1=[]
word2=[]
for x in range(len(str1)):
    word1.append(str1[x])
for x in range(len(str2)):
    word2.append(str2[x])
if(len(word1)==len(word2)):
    for letter in word1:
        if letter in word2:
            word2.remove(letter)

if len(word2)==0:
    print("anagram")
else:
    print("not anagram")



