# a=[1,2,3,4]
# a=iter(a)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(next(a))
# print(next(iter(a)))

class ten:
    def __init__(self):
        self.a=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.a<=10:
            b=self.a
            self.a+=1
            return b
        else:
            raise StopIteration
            
            
t=ten()
for i in t:
    print(i)
