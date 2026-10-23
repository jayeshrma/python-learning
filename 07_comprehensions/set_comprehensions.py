menu = [
    "Black Coffee",
    "Iced Lemon Tea",
    "Cappuccino",
    "Black Coffee"
]

beverages = {beverage for beverage in menu}
print(beverages)
beverages = {beverage for beverage in menu if len(beverage)>12}
print(beverages)


cafe = {
    "Black Coffee": ["Water","Coffee"],
    "Cappuccino": ["Milk","Water","Coffee"],
    "Latte": ["Milk","Chocolate","Coffee"],
    "Matcha": ["Matcha","Water"]
}

unique_items={item for ingredients in cafe.values() for item in ingredients}
print(unique_items)