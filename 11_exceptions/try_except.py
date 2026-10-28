menu={"Pizza":50, "Pasta":80}

try:
    menu["Burger"]
except KeyError:
    print("There is a key error")
    
print("Execution Continues")  