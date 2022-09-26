import threading;
import time as time;

def Thread1(num):
    for i in range(4):
	    print("Thread 1 is running at {}" .format(i*5))
	    time.sleep(5)
    print("Thread 1 is running at {}" .format(20))
    
def Thread2(num):
    for i in range(8):
    	print("Thread 2 is running at {}" .format(i*5))
    	time.sleep(5)
    print("Thread 2 is running at {}" .format(40))
    
def Thread3(num):
    for i in range(7):
    	print("Thread 3 is running at: {}" .format(i*5))
    	time.sleep(5)
    print("Thread 3 is running at {}" .format(35))
    time.sleep(3)
    print("Thread 3 is running at {}" .format(38))

t1 = threading.Thread(target=Thread1, args=(10,))
t1_sub = threading.Thread(target=Thread1, args=(15,))
t2 = threading.Thread(target=Thread2, args=(20,))
t3 = threading.Thread(target=Thread3, args=(30,))

t1.start()
t3.start()
t1.join()
t2.start()
t3.join()
t1_sub.start()

#sudharma kumar