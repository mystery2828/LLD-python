from hotel_management.services.reservation_interface import ReservationInterface
from hotel_management.models.reservation_model import Reservation
import time

class ReservationService(ReservationInterface):
    reservationData = {}
    def makeReservation(self, guest, room):
        reservation = Reservation(guest, room)
        id = time.time_ns
        self.__class__.reservationData[id] = reservation
        room.setIsOccupied()
        return reservation
    
    def checkAvailability(self, room):
        return not room.getIsOccupied()