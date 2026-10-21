import recipies.flavours
print(recipies.flavours.cheesecake())
print(recipies.flavours.donut())

from recipies.flavours import cheesecake, donut
print(donut(),cheesecake())