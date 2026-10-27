class coffee:
    pass

class snack:
    pass

print(type(coffee))

americano=coffee()
print(type(americano))

print(type(americano) is coffee)
print(type(americano) is snack)