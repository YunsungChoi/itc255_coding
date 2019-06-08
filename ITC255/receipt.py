from order import Order
from menu import Menu


class Receipt():
    def __init__(self, menuList, totalprice, orderTime, orderDate):
        self.menuList=menuList
        self.totalprice=totalprice
        self.orderTime=orderTime
        self.orderDate=orderDate

    def print(self):
        resp1 = "Order Time:" + self.orderTime + "Order Date" + self.orderDate
        resp2 = "You got" + self.menuList + "and the Total will be" + self.totalprice
        return resp1 + resp2

