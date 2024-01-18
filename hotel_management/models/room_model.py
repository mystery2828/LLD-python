class Room(object):
    def __init__(self, id, capacity, cost, isOccupied):
        self.id = id
        self.capacity = capacity
        self.cost = cost
        self.isOccupied = isOccupied
    
    def getId(self):
        return self.id
    
    def getCapacity(self):
        return self.capacity
    
    def getCost(self):
        return self.cost
    
    def getIsOccupied(self):
        return self.isOccupied
    
    def setIsOccupied(self):
        print("Room is being marked occupied")
        self.isOccupied = not self.isOccupied
        return self.isOccupied