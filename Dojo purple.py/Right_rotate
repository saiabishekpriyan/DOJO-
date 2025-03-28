n, m = map(int, input().split())  
arr = list(map(int, input().split()))

m = m % n  

for _ in range(m):  
    last = arr[n - 1]  
    for j in range(n - 1, 0, -1):  
        arr[j] = arr[j - 1]  
    arr[0] = last  

print(*arr)
