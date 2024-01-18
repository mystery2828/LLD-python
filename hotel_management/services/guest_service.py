from hotel_management.services.guest_interface import GuestInterface
from hotel_management.models.guest_model import Guest

class GuestService(GuestInterface):
    guests = {}
    def addGuest(self, id, name):
        guest = Guest(id, name)
        self.__class__.guests[id] = guest
        return guest