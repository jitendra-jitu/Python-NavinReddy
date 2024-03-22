class a:
    def __init__(self):
        print("in a")
    def f1(self):
        print("feature 1")
    def f2(self):
        print("feature 2")
class b:
    def __init__(self):
        super()
        print("in b")
    def f3(self):
        print("feature 3")
    def f4(self):
        print("feature 4")
class c(a,b):
    def f5(self):
        super().f4()
a1=c()
