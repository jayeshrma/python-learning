def serve(order):
    try:
        print(f"Preparing {order} order...")
        if order=="unkown":
            raise ValueError("That order is not available")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{order} is served")
    finally:
        print("Next customer please..")