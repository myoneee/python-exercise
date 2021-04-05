#문제2
class AwesomeCal:
    def __init__(self,v):
        self.value = v
    def add(self,v):
        self.value += v
    def sub(self,v):
        self.value -= v
    def mul(self,v):
        self.value *= v
    def div(self,v):
        if v == 0:
            self.value = -9999
        else :
            self.value /= v
    def changeVal(self, v):
        self.value = v

a = AwesomeCal(100)
a.add(5)
print(a.value)     # 105
a.sub(10)
print(a.value)     # 95
a.changeVal(30)
a.mul(5) 
print(a.value)     # 150
a.div(0) 
print(a.value)     # -9999
