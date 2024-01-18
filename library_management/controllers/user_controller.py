class UserController(object):
    def __init__(self, userService):
        self.userService = userService
    
    def addUser(self, id, name, currOwned=None):
        self.userService.addUser(id, name, currOwned)
    
    def removeUser(self, id):
        self.userService.removeUser(id)
    
    def getUsers(self):
        return self.userService.getUsers()