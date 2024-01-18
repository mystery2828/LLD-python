from online_shopping.services.user_interface import UserInterface
from online_shopping.models.user_model import User

class UserService(UserInterface):
    userData = {}
    def addUser(self,id):
        user = User(id)
        self.__class__.userData[id] = user
        return user
    
    def getUsers(self):
        return self.__class__.userData