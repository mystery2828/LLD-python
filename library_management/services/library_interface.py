import abc

class LibraryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addLibrary(self, id, name, books):
        pass

    @abc.abstractmethod
    def removeLibrary(self, id):
        pass
    
    @abc.abstractmethod
    def getLibraryBooks(self):
        pass