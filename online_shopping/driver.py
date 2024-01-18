import sys
sys.path.append('/Users/akash/Desktop/learnings/LLD')

from online_shopping.services.user_service import UserService
from online_shopping.controllers.user_controller import UserController
from online_shopping.services.product_service import ProductService
from online_shopping.controllers.product_controller import ProductController
from online_shopping.services.cart_service import CartService
from online_shopping.controllers.cart_controller import CartController

user_controller = UserController(UserService())
u1 = user_controller.addUser(1)
u2 = user_controller.addUser(2)
u3 = user_controller.addUser(3)
u4 = user_controller.addUser(4)
# print(user_controller.getUsers())

product_controller = ProductController(ProductService())
p1 = product_controller.addProduct(1, "Lizol", 50)
p2 = product_controller.addProduct(2, "Harpic", 80)
p3 = product_controller.addProduct(3, "Lemon Tea", 60)
p4 = product_controller.addProduct(4, "Bru Coffee", 65)
p5 = product_controller.addProduct(5, "Medimix soap", 30)
p6 = product_controller.addProduct(6, "Colgate", 50)
# all_products = product_controller.getProducts()
# for product in all_products:
#     print(all_products[product].getName(), all_products[product].getCost())
    
cart_controller = CartController(CartService())
c1 = cart_controller.addCart(1, u1)
c2 = cart_controller.addCart(2, u4)
c3 = cart_controller.addCart(3, u1)
c4 = cart_controller.addCart(4, u2)
# all_active_carts = cart_controller.getActiveCarts(u1.getId())
# for active_cart in all_active_carts:
#     print(active_cart)
    
cart_controller.addProductToCart(1,1)
cart_controller.addProductToCart(1,3)
current_cart = cart_controller.getCartById(1)
for products in current_cart.getProducts():
    print(products.getName())