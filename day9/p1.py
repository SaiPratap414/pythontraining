from time import sleep
import threading
def f1():
    for i in range(3):
        sleep(2)
        print("This is function f1")
def f2():
    for i in range(3):
        sleep(3)
        print("This is function f2")       
threading.Thread(target=f1).start()
threading.Thread(target=f2).start()

print("main program")