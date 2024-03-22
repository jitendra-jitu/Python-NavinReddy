a=[2,4,6,7,6,5,0,1,3]
for i in range(len(a)-1,1,-1):
    for j in range(i):
        if a[i]<a[j]:
            y=a[i]
            a[i]=a[j]
            a[j]=y
print(a)
