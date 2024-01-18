from library_management.services.user_interface import UserInterface
from library_management.models.user_model import User

class UserService(UserInterface):
    userData = {}
    def addUser(self, id, name, currOwned = None):
        user = User(id, name, currOwned)
        self.__class__.userData[id] = user
        return user

    def removeUser(self, id):
        if id in self.__class__.userData:
            del self.__class__.userData[id]
    
    def getUsers(self):
        return self.__class__.userData