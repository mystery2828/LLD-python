from splitwise.services.group_interface import GroupInterface
from splitwise.models.group_model import Group

class GroupService(GroupInterface):
    groupDetails = {}
    def addGroup(self, id, name, members):
        group = Group()
        group.setId(id)
        group.setName(name)
        group.setMembers(members)
        self.__class__.groupDetails[id] = group
        return group