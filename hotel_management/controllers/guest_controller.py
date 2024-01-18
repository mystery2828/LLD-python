class GuestController(object):
    def __init__(self, guestService):
        self.guestService = guestService
    
    def addGuest(self, id, name):
        self.guestService.addGuest(id, name)