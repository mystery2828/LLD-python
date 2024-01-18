class User:
    def __init__(self, id, name, ownedBook=None):
        self.id = id
        self.name = name
        self.ownedBook = ownedBook
    
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id
        return self.id

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        return self.name
    
    def setOwnedBook(self, ownedBook):
        self.ownedBook = ownedBook
        return self.ownedBook
    
    def getOwnedBook(self):
        return self.ownedBook