file=open("order.txt", "w")
try:
    file.write("Writing from this file")
finally:
    file.close()

## File handling without try-catch

with open("menu.txt", "w") as file2:
    file2.write("Menu is being prepared...")