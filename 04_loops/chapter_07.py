# Walrus Operator
value=13
if (remainder := value%5):
    print(f"Not divisible, the remainder is {remainder}")
    
available_sizes=["Small", "Medium", "Large"]

if (requested_size := input("Enter servong size")) in available_sizes:
    print("Available")
else:
    print("Not available")
    
flavours=["Chocolate", "vanila", "coffee"]
print("Available Falvours", flavours)

if (flavour:= input("Choose your flavour")) not in flavours:
    print("Choose an available flavour")
print(f"You chose {flavour} icecream") # Note access is there even after the block