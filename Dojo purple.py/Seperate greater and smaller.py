n=int(input())
arr=input().split()
target=int(input())

greater=[]
lesser=[]

for i in range(n):
    num=int(arr[i])
    
    if num>target:
        greater.append(num)
        
    else:
        lesser.append(num)
        
print(*greater)
print(*lesser)