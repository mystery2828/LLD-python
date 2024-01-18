class UserController(object):
    def __init__(self, userService):
        self.userService = userService
    
    def addUser(self, id):
        return self.userService.addUser(id)
    
    def getUsers(self):
        return self.userService.getUsers()
        