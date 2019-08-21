def anagram(str1,str2) :
	if sorted(str1)==sorted(str2) :
		print("Yes")
	else :
		print("No")
str1=input()
str2=input()
anagram(str1,str2)
