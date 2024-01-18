class RoomController(object):
    def __init__(self, roomService):
        self.roomService = roomService
    
    def addRoom(self, id, capacity, cost, isOccupied):
        return self.roomService.addRoom(id, capacity, cost, isOccupied)
    
    def checkAvailability(self, id):
        return self.roomService.checkAvailability(id)