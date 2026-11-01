import threading
import time

def takeOrder():
    for i in range(1,4):
        print(f"Taking order #{i}")
        time.sleep(2)
        
def prepOrder():
    for i in range(1,4):
        print(f"Preparing order #{i}")
        time.sleep(3)
        
orderThread=threading.Thread(target=takeOrder)
prepThread=threading.Thread(target=prepOrder)

# Starting the Thread
orderThread.start()
prepThread.start()

# Waiting for the thread to finish
orderThread.join()
prepThread.join()