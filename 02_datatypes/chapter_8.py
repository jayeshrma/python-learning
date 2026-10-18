ingredients=["milk","tea","sugar"]
ingredients.append("sugar")
print(ingredients)
ingredients.remove("tea")


listA=[1,2]
listB=[3,4]
listA.extend(listB)
print(listA)

listA.insert(2,100)
listA.remove(3)
listB.pop()
listB.reverse()
print(listA)


base_liquid=["milk", "water"]
extra=["ginger"]
print(base_liquid+extra)
print(extra*3)


day=bytearray(b"MONDAY")
day=day.replace(b"MON", b"WEDNES")
print(day)

