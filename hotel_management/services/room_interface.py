import abc

class RoomInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addRoom(id, capacity, cost, isOccupied):
        pass
    
    @abc.abstractmethod
    def bookRoom(id):
        pass
    
    @abc.abstractmethod
    def checkAvailability(self, id):
        pass