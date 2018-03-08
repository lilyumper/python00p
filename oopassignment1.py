class Bike(object):
    def __init__(self,price,max_speed,miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    
    def displayinfo(self):
        print "The price is {}".format(self.price)
        print "The Max speed is {}".format(self.max_speed) + " mph"
        print "Your total miles are {} ".format(self.miles)
        return self
    
    def ride(self):
        print "Riding"
        self.miles +=10
        return self
    
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles <=0:
            print "Your BIKE BROKE!!!"
            self.miles = 0
        return self

bike1 = Bike("$50.99", "15",250)
bike1.ride().ride().ride().reverse().displayinfo()

bike2 = Bike("$100.00", "25", 0)
bike2.ride().reverse().reverse().displayinfo()

bike3= Bike("$150.88", "30", 250)
bike3.reverse().displayinfo()





