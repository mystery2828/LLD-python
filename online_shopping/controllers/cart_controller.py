class CartController(object):
    def __init__(self, cartService):
        self.cartService = cartService
    
    def addCart(self, id, user, products = [], cartTotal = 0):
        return self.cartService.addCart(id, user, products, cartTotal)
    
    def getActiveCarts(self, userId):
        return self.cartService.getActiveCarts(userId)

    def addProductToCart(self, cartId, productId):
        return self.cartService.addProductToCart(cartId, productId)
    
    def getCartById(self, cartId):
        return self.cartService.getCartById(cartId)