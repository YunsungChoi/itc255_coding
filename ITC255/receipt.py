
from menu import Menu


class Receipt():
    def __init__(self, menuList, totalprice):
        self.menuList=menuList
        self.totalprice=totalprice


    def print(self):
        resp2 = "You got" + self.menuList + "and the Total will be" + self.totalprice
        return  resp2

