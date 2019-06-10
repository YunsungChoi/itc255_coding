import unittest
from payment import Payment
from menu import Menu
from cart import Cart
from receipt import Receipt
from order import Order



class MenuTest(unittest.TestCase):
    def setUp(self):
        self.menu=Menu('poke', 'Available', 12.06, 1, 'Contains Raw fishes')

    def test_string(self):
        self.assertEqual(str(self.menu),self.menu.menuName)

    def test_getPrice(self):
        self.assertEqual(str(self.menu.getMenuPrice()), '12.06')

    def test_getmenuNumber(self):
        self.assertEqual(str(self.menu.getMenuNum()),'1')
    
    def test_getMenuNote(self):
        self.assertEqual(str(self.menu.getMenuNote()),'Contains Raw fishes')

class OrderTest(unittest.TestCase):

   def setUp(self):
       self.order=Order()
       self.menu1=Menu('pokeS', 'Available', 12.06, 1, 'Contains Raw fishes')
       self.menu2=Menu('pokeM', 'Available', 14.26, 1, 'Contains Raw fishes')
       self.menu3=Menu('pokeL', 'Available', 16.46, 1, 'Contains Raw fishes')

       self.cart1=Cart(self.menu1,1)
       self.cart2=Cart(self.menu2,3)
       self.cart3=Cart(self.menu3,2)

       
       self.order.addMenu(self.cart1)
       self.order.addMenu(self.cart2)
       self.order.addMenu(self.cart3)

   def test_addandGetOrderMenus(self):
    
       self.ordermenus=self.order.getMenu()
       self.assertEqual(len(self.ordermenus),3)

   def test_CalculateTotal(self):
        payment=self.order.calcTotal()
        self.assertEqual(str(payment), 'Your Total will be 87.76')

class CartTest(unittest.TestCase): 
    def setUp(self):
        self.menu=Menu('pokeS', 'Available', 12.06, 1, 'Contains Raw fishes')
        self.cart=Cart(self.menu,1)

    def test_Quantity(self):
        self.assertEqual(self.cart.getQuantity(),1)
    
    def test_Menu(self):
        menu=self.cart.getMenu()
        self.assertEqual(str(menu), 'pokeS')
