from online_shopping.services.cart_interface import CartInterface
from online_shopping.models.cart_model import Cart
from online_shopping.services.product_service import ProductService

class CartService(CartInterface):
    cartsData = {}
    def addCart(self, id, user, products = [], cartTotal = 0):
        cart = Cart(id, user)
        self.__class__.cartsData[id] = cart
        return cart

    def getActiveCarts(self, userId):
        activeCarts = []
        for cart in self.__class__.cartsData:
            if userId == self.__class__.cartsData[cart].getUser().getId():
                activeCarts.append(self.__class__.cartsData[cart])
        return activeCarts
    
    def addProductToCart(self, cartId, productId):
        product_service = ProductService()
        productDetails = product_service.getProductById(productId)
        self.__class__.cartsData[cartId].addProduct(productDetails)
        updatedTotal = self.__class__.cartsData[cartId].getCartTotal() + productDetails.getCost()
        self.__class__.cartsData[cartId].setCartTotal(updatedTotal)
        print("added product to cart")
        
    def getCartById(self, id):
        return self.__class__.cartsData[id]