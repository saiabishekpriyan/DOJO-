def sortcolours(a):
    low,mid,high=0,0,len(a)-1

    while mid<=high:
        if a[mid]==0:
            a[mid],a[low]=a[low],a[mid]
            mid+=1
            low+=1
        elif a[mid]==1:
            mid+=1
        else:
            a[mid],a[high]=a[high],a[mid]
            high-=1

a=list(map(int,input().split()))
sortcolours(a)
print(*a)