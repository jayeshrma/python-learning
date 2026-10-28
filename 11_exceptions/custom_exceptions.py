class OutOfStockError(Exception):
    pass

def serve(order):
    if order != "pizza":
        raise OutOfStockError(f"{order} is out of stock")