def order(item, quantity):
    try:
        menu={"burger":120}[item]
        print(f"Total Cost is :{item*quantity}")
    except KeyError:
        print("Item not in menu")
    except TypeError:
        print("quantity should be a number")