class Group(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.members = []
        
    def setId(self, id: int) -> int:
        self.id = id

    def getId(self) -> None:
        return self.id
    
    def setName(self, name: str) -> None:
        self.name = name
    
    def getName(self) -> str:
        return self.name

    def setMembers(self, members: list) -> None:
        self.members = members
    
    def getMembers(self) -> list:
        return self.members