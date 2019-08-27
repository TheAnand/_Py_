size = int(input())
arr1 = list(map(int , input().strip().split()))
arr2 = list(map(int , input().strip().split()))
arr = []
for i in range(size) :
    temp=int(arr1[i] + arr2[i])
    arr.append(temp)
    print(arr[i],end=" ")
