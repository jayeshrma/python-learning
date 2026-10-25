def serveCoffee():
    print("Welcome to coffee Shop!") # Just runs once
    order=yield
    
    while True:
        print(f"Serving: {order}")
        order=yield 

server=serveCoffee()
next(server) # starting generator

server.send("Americano")
server.send("Latte")

# The yield keyword stops further execution until the next send.
# Without that it would be an infinite loop.