#method1 (not efficient)

# def sum(*args):
#     if type(args[0])==int:
#         ans=0
#     if type(args[0])==str:
#         ans=""
#     for i in args:
#         ans=ans+i
#     return ans
# print(sum(5,4,6))
# print(sum("a","d","d"))

#method2

# def sum(a=None, b=None ,c=None):
#     s=0
#     if a!=None and b!=None and c!=None:
#         s=a+b+c
#     elif a!=None and b!=None:
#         s=a+b
#     else:
#         s=a
#     print(s)
# sum(2,3,4)

#method3(most efficient method)
""" from multipledispatch import *

@dispatch(float,float,float)
def sum(a,b,c):
    s=a+b+c
    print(s)

sum(2.0,3.0,4.0)


@dispatch(int ,int,int,int)
def sum(a,b,c,d):
    s=a+b+c+d
    print(s)

sum(2,3,4,4)

 """

