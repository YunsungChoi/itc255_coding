class Menu():
    def __init__(self, menuName, menuAvailability, menuPrice, menuNum, menuNote):
        self.menuName=menuName
        self.menuAvailability=menuAvailability
        self.menuNum=menuNum
        self.menuPrice=menuPrice

        self.menuNote=menuNote

    def getMenu(self):
        return self.menuName

    def getMenuNum(self):
        return self.menuNum
    
    def getMenuPrice(self):
        return self.menuPrice

    def getMenuNote(self):
        return self.menuNote

    def __str__(self):
        return self.menuName