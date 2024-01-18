class ProductController(object):
    def __init__(self, productService):
        self.productService = productService
        
    def addProduct(self, id, name, cost):
        return self.productService.addProduct(id, name, cost)
    
    def getProducts(self):
        return self.productService.getProducts()