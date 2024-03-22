#iterative method
""" def binarysearch(a,n):
    a.sort()
    l=0
    h=len(a)-1
    mid=(l+h)/2
    i=0
    while i<h:
        mid=(l+h)//2
        if n==a[mid]:
            return True
        else:    
            if n<a[mid]:
                h=mid
            else:
                l=mid
        i+=1
    return False
b=[17,16,15,14,13,12,11]
n=int(input())
if binarysearch(b,n):
    print(n,"is found ")
else:
    print("not found")
"""




#recurive method

# def binarysearch(l,h,a,n):            
#     if h>=l:          
#         mid=(l+h)//2
#         if n==a[mid]:
#             return True
            
#         elif a[mid]>n:
#             h=mid-1
#             return binarysearch(l,h,a,n)
#         else:
#             l=mid+1
#             return binarysearch(l,h,a,n)
#     else:
#         return False
# b=[1,3,5,6,9]
# n=int(input())

# if binarysearch(0,len(b)-1,b,n):
#     print(n," is found")
# else:
#     print("not found")
    