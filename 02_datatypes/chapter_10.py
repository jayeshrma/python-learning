chai_order=dict(type="masala_Chai", amount="large", sugar=2);
print(chai_order)

chai_recipe={}
chai_recipe['base']="milk"
chai_recipe['extra']="lemon"
del chai_recipe["base"]

print(chai_recipe["extra"])

print(chai_order.keys())
print(chai_order.values())
print(chai_order.items())

last_item=chai_order.popitem()

extra_spices={"cardamom":"crushed", "ginger":"sliced"}
chai_recipe.update(extra_spices)
print(chai_recipe)

# Safe get , doesnot crash the application
customer_note=chai_order.get("note", "No note")