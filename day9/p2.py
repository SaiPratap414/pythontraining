import threading
from time import sleep

def cube(x):
    for i in range(3):
        sleep(2)
        print(x*x*x)
        
def square(x):
    for i in range(3):
        sleep(3)
        print(x*x)
t1 = threading.Thread(target=cube, args=(2,))
t2 = threading.Thread(target=square, args=(3,))
t1.start()
t2.start()