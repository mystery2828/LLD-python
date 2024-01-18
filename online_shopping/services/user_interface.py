import abc

class UserInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addUser(self,id):
        pass
    
    @abc.abstractmethod
    def getUsers(self):
        pass