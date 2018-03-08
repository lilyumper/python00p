class MathDojo(object):
    def __init__(self):
        self.value = 0
    
    def add(self,*num):
        for i in num:
            if type(i) == int:
                print i
                self.value += i
            elif type(i) == tuple or list:
                for z in i:
                    self.value +=z

                
        return self
    
    def subtract(self,*num1):
        for i in num1:
            if type(i) == int:
                print i
                self.value -= i
            elif type(i) == tuple or list:
                for z in i:
                    self.value -=z
        return self
    def result(self):
        print self.value
    
md =MathDojo()
md.add(2).add(2,5,6,6,6).subtract(3,2).add([2,3.2,4]).result()
        
