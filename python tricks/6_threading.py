import time
from threading import Thread

def print1():
    print("Hello world!, now wait for 3 seconds")
    time.sleep(3)
    print("Did this")

def print2():
    print("Hello world! again")
    time.sleep(4)
    print("Did that")

Thread1 = Thread(target=print1)
Thread1.start()
Thread2 = Thread(target=print2)
Thread2.start()


#you can use threading to run multiple codes in background
#you can start one function and while that function in running, you can start another function
