from multiprocessing import Process
import time

def crunchNumber():
    print("Started Counting Process")
    count=0
    for _ in range(100_000_000):
        count+=1
    print("Ended Counting Process")
    
if __name__=="__main__":
    
    start=time.time()
    
    p1=Process(target=crunchNumber)
    p2=Process(target=crunchNumber)
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    end=time.time()
    
    print(f"Total time: {end-start}")