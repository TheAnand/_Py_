from collections import Counter
N=int(input())
arr= list(map(int, input().strip().split(" "))[:N])
C = Counter(arr)
q=int(input())
for _ in range(q):
	n = int(input())
	print(C[n] if C[n] > 0 else "NOT PRESENT")
