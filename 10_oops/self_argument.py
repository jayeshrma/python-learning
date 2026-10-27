class Bottle:
    capacity=150 #ml
    
    def describe(self):
        print(f"Capacity is {self.capacity} ml")
    
waterBottle=Bottle()
waterBottle.describe()

Bottle.describe()
Bottle.describe(waterBottle)