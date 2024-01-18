import abc

class GroupInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addGroup(self, id, name, members):
        pass