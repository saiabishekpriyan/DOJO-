n=int(input())
arr1=list(map(int,input().split()))
arr2=[]

for element in arr1:
    arr2.append(element)
    
print(*arr2)