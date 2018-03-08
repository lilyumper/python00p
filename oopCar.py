class Car(object):
    def __init__(self,price,speed,fuel,milelage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milelage = milelage
        self.tax = ""
        if self.price > 10000:
            self.tax = "15%"
        else:
            self.tax = "12%"
        self.displayall()
    
    def displayall(self):
        print "Your price is ${}".format(self.price)
        print "Your speed is {} mph".format(self.speed)
        if self.fuel == 100:
            print "Fuel: Full Tank"
        elif self.fuel <=99 and self.fuel >= 75:
            print "Fuel: 3/4 Tank"
        elif self.fuel <=74 and self.fuel >=50:
            print "Fuel: Half Tank"
        elif self.fuel <=49:
            print"Fuel: Low"
        print "Milelage: {}".format(self.milelage)
        print "Tax: {}".format(self.tax)
        return self
            

Buick =Car(11000,"75",75,"1125")


car2 = Car(5000,"45",100,"150")

car3 = Car(25000,"55",46,"0")

car4 = Car(9999,"15",100,"35000")


