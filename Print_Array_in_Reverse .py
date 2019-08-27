lst = []
n = int(input()) #Enter size of list
def Rev(lst) :
	lst.reverse()	 #reverse list
	for i in range(n) :
		print(lst[i])	#print list one by one

for i in range(n) :
	ele = int(input())
	lst.append(ele)		#append values in list
Rev(lst)
