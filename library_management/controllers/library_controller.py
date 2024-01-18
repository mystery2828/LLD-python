class LibraryController(object):
    def __init__(self, libraryService):
        self.libraryService = libraryService
    
    def addLibrary(self, id, name, books={}):
        self.libraryService.addLibrary(id, name, books)