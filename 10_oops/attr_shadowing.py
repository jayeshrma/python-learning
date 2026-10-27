class Waffle:
    flavour="chocolate"
    sprinkles="Yes"
    
tripleChoco=Waffle()

tripleChoco.sprinkles="No"
print(tripleChoco.sprinkles)
print(Waffle.sprinkles)

del tripleChoco.sprinkles
print(tripleChoco.sprinkles)

tripleChoco.syrup="vanilla"
del tripleChoco.syrup
print(tripleChoco.syrup)