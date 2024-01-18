class Cart(object):
    def __init__(self, id, user, products = [], cartTotal = 0):
        self.id = id
        self.user = user
        self.products = products
        self.cartTotal = cartTotal
        
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getUser(self):
        return self.user
    
    def getProducts(self):
        return self.products
    
    def getCartTotal(self):
        return self.cartTotal
    
    def setCartTotal(self, cartTotal):
        self.cartTotal = cartTotal
        return self.cartTotal

    def addProduct(self, product):
        self.products.append(product)