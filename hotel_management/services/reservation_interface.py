import abc

class ReservationInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def makeReservation(self, guest, room):
        pass
    
    @abc.abstractmethod
    def checkAvailability(self, room):
        pass
    