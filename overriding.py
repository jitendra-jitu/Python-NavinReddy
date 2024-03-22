class durga():
    def __init__(self):
        print("durga ")
    def show(self):
        print("durga-grandparent")
class jyothi(durga):
    def __init__(self):
        super().__init__()
        print("jyothi")
    def show(self):
        print("jyothi-parent")
        super().show()
class jitu(jyothi):
    def __init__(self):
        super().__init__()
        print("jitu")
    def show(self):
        print("jitu-chikd")
        super().show()

j=jitu()
j.show()





