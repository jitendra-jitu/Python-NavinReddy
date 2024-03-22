from abc import ABC,abstractmethod
class jitu(ABC):
    def __init__(self):
        self.a="btech"
    @abstractmethod
    def study(self):
        pass
class jitu_details(jitu):
    def name(self):
        return "jitendra"
    def study(self):
        return self.a
j=jitu_details()
print(j.study())
