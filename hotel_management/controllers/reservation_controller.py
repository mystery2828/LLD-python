class ReservationController(object):
    def __init__(self, reservationService):
        self.reservationService = reservationService
    
    def makeReservation(self, guest, room):
        self.reservationService.makeReservation(guest, room)
        
    def checkAvailability(self, room):
        return self.reservationService.checkAvailability(room)