from library_management.services.book_interface import BookInterface
from library_management.models.book_model import Book

class BookService(BookInterface):
    booksData = {}
    def addBook(self, id, name, currLibrary, prevOwned = [], currOwned = None):
        book = Book(id, name, currLibrary, prevOwned, currOwned)
        if id not in self.__class__.booksData:
            self.__class__.booksData[id] = book
        return book
    
    def removeBook(self, id):
        if id in self.__class__.booksData:
            del self.__class__.booksData[id]
            
    def getBooks(self):
        return self.__class__.booksData