class BookController(object):
    def __init__(self, bookService):
        self.bookService = bookService
    
    def addBook(self, id, name, currLibrary, prevOwned = [], currOwned = None):
        self.bookService.addBook(id, name, currLibrary, prevOwned, currOwned)
        
    def getBooks(self):
        return self.bookService.getBooks()