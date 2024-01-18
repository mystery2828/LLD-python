class UserController(object):
    def __init__(self, userService) -> None:
        self.userService = userService
    
    def addUser(self, id, name):
        return self.userService.addUser(id, name)