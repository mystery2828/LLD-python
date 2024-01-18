import abc

class UserInterface(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def addUser(self, id, name):
        pass