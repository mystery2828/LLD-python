from splitwise.services.bill_interface import BillInterface
from splitwise.models.bill_model import Bill

class BillService(BillInterface):
    billDetails = {}
    def addBill(self, id, group, contribution, paidBy):
        bill = Bill()
        bill.setId(id)
        bill.setGroup(group)
        bill.setContribution(contribution)
        bill.setPaidBy(paidBy)
        self.__class__.billDetails[id] = bill
        return bill