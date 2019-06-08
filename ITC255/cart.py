from menu import Menu

class Cart():
    def __init__(self,menu, quantity):
        self.menu=menu
        self.quantity=quantity

    def getMenu(self):
        return self.menu

    def getQuantity(self):
        return self.quantity