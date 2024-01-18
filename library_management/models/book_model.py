class Book(object):
    def __init__(self, id, name, currLibrary, prevOwned=[], currOwned=None):
        self.id = id
        self.name = name
        self.currLibrary = currLibrary
        self.prevOwned = prevOwned
        self.currOwned = currOwned
    
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

    def getCurrLibrary(self):
        return self.currLibrary
    
    def setCurrLibrary(self, currLibrary):
        self.currLibrary = currLibrary
        return self.currLibrary

    def getPrevOwned(self):
        return self.prevOwned

    def setPrevOwned(self, prevOwned):
        self.prevOwned = prevOwned
        return self.prevOwned

    def getCurrOwned(self):
        return self.currOwned
    
    def setCurrOwned(self, currOwned):
        self.currOwned = currOwned
        return self.currOwned
