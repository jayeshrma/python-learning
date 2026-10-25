def snacks():
    yield "Buger"
    yield "Fries"
    
def drinks():
    yield "Mocktail"
    yield "MilkShake"

def menu():
    yield from snacks()
    yield from drinks()
    
server=menu()
for item in server:
    print(item)
    
    
def serve():
    try:
        while True:
            order=yield "Waiting for order"
    except:
        print("Shop is closed")
        
server=serve()
print(next(server))

server.close() # cleanup