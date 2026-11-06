import threading
import time

def monitor():
    while True:
        print(f"Montinoring...")
        time.sleep(3)
        
t=threading.Thread(target=monitor, daemon=True)
t.start()