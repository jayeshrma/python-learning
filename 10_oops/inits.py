class Order:
    def __init__(self,type_,size):
        self.type=type_
        self.size=size
        
    def summary(self):
        print(f"Summary : {self.size} ml of {self.type}")

order1=Order("Latte", 150)
order1.summary()