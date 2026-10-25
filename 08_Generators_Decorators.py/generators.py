def serve():
    yield "Serving 1"
    yield "Serving 2"
    yield "Serving 3"
    
server=serve()
print(server)

for serving in server:
    print(serving)

server2=serve()
print(next(server2))
print(next(server2))