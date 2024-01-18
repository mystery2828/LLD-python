import abc

class GuestInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addGuest(self, id, name):
        pass
    