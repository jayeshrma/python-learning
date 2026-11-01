from multiprocessing import Process
import time

def order(name):
    print(f"Start of the order {name}")
    time.sleep(3)
    print(f"Finish of the order {name}")
    
if __name__== "__main__":
    orderMaker=[
        Process(target=order, args=(f"Order #{i+1}"))
        for i in range(3)
    ]
    
    # Start all process
    for p in orderMaker:
        p.start()
        
        
    # Wait for all to complete
    for p in orderMaker:
        p.join()
    