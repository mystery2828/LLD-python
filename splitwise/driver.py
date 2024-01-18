import sys
sys.path.append('/Users/akash/Desktop/learnings/LLD')
from splitwise.controllers.user_controller import UserController
from splitwise.controllers.bill_controller import BillController
from splitwise.controllers.group_controller import GroupController

from splitwise.services.user_service import UserService
from splitwise.services.bill_service import BillService
from splitwise.services.group_service import GroupService


user_controller = UserController(UserService())
user1 = user_controller.addUser(1,"akash")
user2 = user_controller.addUser(2,"hardik")
user3 = user_controller.addUser(3,"pruthvik")
user4 = user_controller.addUser(4,"nishanth")


group_controller = GroupController(GroupService())
badminton_members = [user1, user2, user3, user4]
group1 = group_controller.addGroup(1,"Badminton",badminton_members)
kengeri_house_members = [user1, user2]
group2 = group_controller.addGroup(2, "Kengeru House", kengeri_house_members)


group1_members = group2.getMembers()
for ele in group1_members:
    print(ele.getName())
    
    
bill_controller = BillController(BillService())
bill_controller.addBill(1,1,{1:100,2:100,3:100,4:100},{1:200,2:200})

print(bill_controller.getUserBalance(1))


bill_controller = BillController(BillService())
bill_controller.addBill(2,2,{1:100,2:100},{1:200})

print(bill_controller.getUserBalance(1))