""" a=10
b=12
c=int.__add__(a,b)
print(c)

class jitu:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        print(m1,m2)
    
j1=jitu(10,10)
j2=jitu(12,13)


j3=j1+j2


 """
class jitu:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __le__(self,other):
        m=self.a+self.b
        n=other.a+other.b
        if m<=n:
            return True
        else:
            return False
j1=jitu(10,10)
j2=jitu(12,13)
if j1<=j2:
    print("lesser")