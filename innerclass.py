class jitu:
    def __init__(self):
        self.j1="jitu class here...!"
        self.puli=self.puli()                               #1 multiple inner class //multilevel innerclass
        
    def show(self):
        print(self.j1)
    class puli:
        def __init__(self):
            self.bindu=self.bindu()
        def show(self):
            print("puli class here...!")          
        class bindu:                              
            def show(self):
                print("bindu class here...!")

        
"""j=jitu()
p=j.puli
p.show()
b=j.bindu
b.show()
"""
j=jitu()
j.show()
puli=j.puli
puli.show()
bindu=puli.bindu
bindu.show()
