# Nonlocal

def updateOrder():
    flavour="Vanilla"
    def updateFlavour():
        nonlocal flavour
        flavour="Strawberry"
    
    updateFlavour()
    print(f"After update : {flavour}")

updateOrder()