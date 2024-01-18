import abc

class BookInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addBook(self, id, name, currLibrary, prevOwned = [], currOwned = None):
        pass
    
    @abc.abstractmethod
    def removeBook(self, id):
        pass
    
    @abc.abstractmethod
    def getBooks(self):
        return self.__class__.booksData