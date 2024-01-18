from splitwise.services.user_inferface import UserInterface
from splitwise.models.user_model import User

class UserService(UserInterface):
    userDetails = {}
    def addUser(self, id, name):
        user = User()
        user.setId(id)
        user.setName(name)
        self.__class__.userDetails[id] = user
        return user
    