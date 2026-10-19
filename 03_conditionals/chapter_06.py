# Match-case conditionals
seat_type=input("Enter seat type: (Sleeper/AC/General/Luxury)").lower()

match seat_type:
    case "sleeper":
        print("Price is 10")
    case "ac":
        print("Price is 20")
    case "general":
        print("Price is 5")
    case "luxury":
        print("Price is 30")
    case _:
        print("Invalid seat type")