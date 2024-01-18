class Product(object):
    def __init__(self, id, name, cost):
        self.id = id
        self.name = name
        self.cost = cost

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getCost(self):
        return self.cost
    
    def setCost(self, cost):
        self.cost = cost