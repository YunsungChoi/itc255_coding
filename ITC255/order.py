from menu import Menu
from cart import Cart
from payment import Payment
from receipt import Receipt

class Order():
    def __init__(self):
        self.cart=[]

    def addMenu(self,cart):
        self.cart.append(cart)

    def getMenu(self):
        return self.cart

    def calcTotal(self):
        total=0.0
        for x in self.cart:
            total += x.getMenu().menuPrice * x.quantity
        payment = Payment(total)
        return payment

