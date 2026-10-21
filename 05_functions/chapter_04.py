# Args & *kwargs
def order(flavour, cream, sprinkles):
    print(flavour, cream, sprinkles)
    
order("Walnut", "White Choco", "Yes") # Positional
order(flavour="Almond", sprinkles="No", cream="Coffee") # keywords

def specialOrder(*ingredients, **extras):
    print(ingredients) # List
    print(extras) # Dictionary
    
specialOrder("Coffee","Walnut",nuts="Yes",sprinkles="No")