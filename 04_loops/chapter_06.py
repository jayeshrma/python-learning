staff=[("Amit",17),("Zara",15),("Raj",16)]

for name,age in staff:
    if age<=18:
        print(f"{name} is below 18")
        break       
else:
    print("No one is below 18")