import abc

class BillInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addBill(self, id, group, contribution, paidBy):
        pass