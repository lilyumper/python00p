class Product(object):
    def __init__(self,price,name,weight,brand,status):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status
        self.tax =.08
    
    def cost(self):
        self.price = ((self.tax)*(self.price)) + self.price
        print self.price
        return self
    
    def whatever(self):
        if self.status == "Have":
            self.status = "For Sale"
        elif  self.status =="Dont have":
            self.status = "Sold"
        return self
    
    def back(self):
        if self.status =="Nasty":
            self.status ="Defective"
        elif self.status == "Open":
            self.status ="used"
        print self.status
        return self

    def info(self):
        print "Brand: {}".format(self.brand)
        print "Item Name: {}".format(self.name)
        print "Weight: {}".format(self.weight)
        return self
    
tuna= Product(4,"Tuna","3 oz","Fishy", "Open")
tuna.cost().whatever().back().info()


    
