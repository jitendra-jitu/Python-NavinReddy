class inheritance:
    def __init__(self) :
        self.name="welcome to my world"
    def show(self):
        return self.name
class inh2(inheritance):
    pass
i=inh2()
print(i.show())
