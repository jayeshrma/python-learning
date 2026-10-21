# Default Trap in Python
# Python Gotcha

def orders(order=[]):
    order.append("Cream")
    print(order)
    
orders()
orders()

# Fix

def orders(order=None):
    if order is None:
        order=[]
    order.append("Cream")
    print(order)
    
    
orders()
orders()