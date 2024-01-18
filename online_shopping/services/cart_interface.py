import abc

class CartInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addCart(self, id, user, products, cartTotal):
        pass
    
    def getActiveCarts(self, userId):
        pass