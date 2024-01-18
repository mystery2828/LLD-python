from library_management.services.library_interface import LibraryInterface
from library_management.models.library_model import Library

class LibraryService(LibraryInterface):
    librariesData = {}
    def addLibrary(self, id, name, books={}):
        library = Library(id, name)
        self.__class__.librariesData[id] = library
        return library

    def removeLibrary(self, id):
        if id in self.__class__.librariesData:
            del self.__class__.librariesData[id]