- Classes: Product, User, Cart, Order, Payment, etc.
- Features: Add to Cart, Place Order, View Order History, Payment Processing.


Product {
    id,
    name,
    unitCost
}

User {
    id
}

Cart {
    id,
    User,
    Products,
    cartTotal
}
