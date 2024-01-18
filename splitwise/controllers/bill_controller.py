class BillController(object):
    def __init__(self, billService):
        self.billService = billService
    
    def addBill(self, id, group, contribution, paidBy):
        self.billService.addBill(id, group, contribution, paidBy)
        
    def getUserBalance(self, userId):
        balance = 0
        for billId in self.billService.billDetails:
            bill = self.billService.billDetails.get(billId)
            if userId in bill.getContribution():
                balance -= bill.getContribution().get(userId)
            if userId in bill.getPaidBy():
                balance += bill.getPaidBy().get(userId)
        return balance