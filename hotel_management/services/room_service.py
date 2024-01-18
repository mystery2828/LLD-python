from hotel_management.services.room_interface import RoomInterface
from hotel_management.models.room_model import Room

class RoomService(RoomInterface):
    roomData = {}
    def addRoom(self,id, capacity, cost, isOccupied):
        room = Room(id, capacity, cost, isOccupied)
        self.__class__.roomData[id] = room
        return room

    def bookRoom(self,room):
        for rooms in self.__class__.roomData:
            if room.id == self.__class__.roomData[rooms].get("id") and self.__class__.roomData[rooms][room.id]["isOccupied"] == False:
                self.__class__.roomData[rooms][room.id]["isOccupied"] = True
                room.setOccupied()
                return True
            else:
                return False
            
    def checkAvailability(self, id):
        print("ID: ", id)
        if id in self.__class__.roomData:
            return self.__class__.roomData[id]