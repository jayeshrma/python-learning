class Pizza:
    def __init__(self,size):
        self.size=size
        
class CheesePizza:
    def __init__(self,size,cheese):
        # self.size=size
        # Pizza.__init__(self,size)
        super.__init__(self,size)
        self.cheese=cheese