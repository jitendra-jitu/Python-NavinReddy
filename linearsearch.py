from array import *
n=int(input())
a=array('i',[1,2,3,4,5,6,7,8,9])
def linearsearch(arr,num):
    for i in range(len(a)):
            if n==a[i]:
                print(a[i],"is found at index:",i)

    if n not in a:
        print(n,"is in not this array")
linearsearch(a,n)
            
