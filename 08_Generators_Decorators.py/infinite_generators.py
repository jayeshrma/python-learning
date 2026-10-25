def infiniteServe():
    count=1
    while True:
        yield f"Serving {count}"
        count+=1
        
server=infiniteServe()

for _ in range(11):
    print(next(server))