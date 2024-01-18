from online_shopping.services.product_interface import ProductInterface
from online_shopping.models.product_model import Product

class ProductService(ProductInterface):
    productsData = {}
    def addProduct(self, id, name, cost):
        product = Product(id, name, cost)
        self.__class__.productsData[id] = product
        return product
    
    def getProducts(self):
        return self.__class__.productsData
    
    def getProductById(self, id):
        return self.__class__.productsData[id]