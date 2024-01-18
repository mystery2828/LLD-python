import abc

class UserInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addUser(self, id, name, currOwned=None):
        pass

    @abc.abstractmethod
    def removeUser(self,id):
        pass
    
    @abc.abstractmethod
    def getUsers(self):
        pass