class Library(object):
    def __init__(self, id, name, books = {}):
        self.id = id
        self.name = name
        self.books = books
    
    def getId(self):
        return self.id

    def getName(self):
        return self.name
    
    def addBooks(self, books):
        for book in books:
            if book.getId() not in self.books:
                self.books[book.getId()] += 1
            else:
                self.books[book.getId()] = book
    
    def getBooks(self):
        return self.books