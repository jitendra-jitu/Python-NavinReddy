# a=10
# b=14
# while b!=0:

#     c=a & b     #  1010                     #00100(4)               #10000(16)
#                 #  1110                     #10100(20)              #01000(8)
    
#                 #  1010(and)10              #00100(and)//4          #00000//0
                                            
#     print(c)
#     a=a^b       #  0100(x0r) 4              #10000(xor)//16         #11000//24


#                 #  10100(b)//20             #01000//8               #00000//0
#     print(a)
#     b=c<<1
#     print(b)
# print(a)

n=int(input())
m=int(input())
c=n^m
n=c^n
m=c^m
print(n)
print(m)