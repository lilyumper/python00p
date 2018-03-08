class Creature(object):
    def __init__(self, name, health):
        self.name = name
        self.health = 150
    
    def walk(self):
        self.health -= 1
        return self
    
    def run (self):
        self.health -=5
        return self
    
    def display_health(self):
        print self.health
    
class Dog(Creature):
    def __init__(self,name):
        super(Dog,self).__init__(name, 170)
    
    def pet(self):
        self.health += 5
        print self.name, self.health
        return self

class Dragon(Creature):
    def __init__(self,name):
        health = 180
        super(Dragon,self).__init__(name, health)
      
    
    def fly(self):
        self.health += 10
        return self
    
    def dragon_health_display(self):
        print  self.name," I am a Dragon {}".format(self.health)
        

dragon1=Dragon("dude")
dragon1.dragon_health_display()

dog1=Dog("rover")
dog1.pet()
