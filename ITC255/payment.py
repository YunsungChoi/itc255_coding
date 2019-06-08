class Payment():
    def __init__(self, payAmount):
        self.payAmount=payAmount

    def __str__(self):
        self.payAmount=round(self.payAmount, 2)
        response="Your Total will be" + str(self.payAmount)
        return response
