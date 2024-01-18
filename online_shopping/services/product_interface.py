import abc

class ProductInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addProduct(self, id, name, cost):
        pass

    @abc.abstractmethod
    def getProductById(self, id):
        pass
    