n=int(input())
arr=list(map(int,input().split()))

uniques=[]*n
count=0

for i in range(n):
    is_duplicate=False
    for j in range(count):
        if arr[i]==uniques[j]:
            is_duplicate=True
            break
    if not is_duplicate:
        uniques[count]=arr[i]
        count+=1

for i in range(count):
    print(uniques[i],end=" ")
print()