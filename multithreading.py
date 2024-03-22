#1

import time                            #multithreading with functions & none arguments
from  threading import *
def hello():
    for i in range(10):
        print("hello")
        time.sleep(1)
def hi():
    for i in range(10):
        print("hi")
        time.sleep(1)
h1=Thread(target=hello,name='h1')
h2=Thread(target=hi)

h1.start()
time.sleep(0.1)
h2.start()

h1.join()
h2.join()
print("threads are done")


#2

# from threading import *                    //multithreading with methods performs certain methods & os
# from os import *
# def hello():
#     print(getpid())
#     print(current_thread().name)
# def hi():
#     print(getpid())
#     print(current_thread().name)
    
# if __name__=="__main__":
# 	print(getpid())
# 	print(current_thread().name)
# 	h1=Thread(target=hello)
# 	h2=Thread(target=hi)
			
# 	h1.start()
# 	h2.start()

# 	h1.join()
# 	h2.join()

# 	print("ok bye!!")


#3

# import concurrent.futures                                             //using concurrent feautures
# def jitu():
#     print("welcome to jitu world")
# pool=concurrent.futures.ThreadPoolExecutor(max_workers=1)

# pool.submit(jitu)
# pool.submit(jitu)
# pool.submit(jitu)
# pool.submit(jitu)
# pool.submit(jitu)
# pool.shutdown(wait=False)
# print("jitu done")




#4

# import threading 

# # global variable x 
# x = 0

# def increment(): 
	
# 	global x 
# 	x += 1

# def thread_task(lock): 
	
# 	for _ in range(100000): 
# 		lock.acquire() 
# 		increment() 
# 		lock.release() 

# def main_task(): 
# 	global x 
# 	# setting global variable x as 0 
# 	x = 0

# 	# creating a lock 
# 	lock = threading.Lock() 

# 	# creating threads 
# 	t1 = threading.Thread(target=thread_task, args=(lock,)) 
# 	t2 = threading.Thread(target=thread_task, args=(lock,)) 

# 	# start threads 
# 	t1.start() 
# 	t2.start() 

# 	# wait until threads finish their job 
# 	t1.join() 
# 	t2.join() 

# if __name__ == "__main__": 
# 	for i in range(10): 
# 		main_task() 
# 		print("Iteration {0}: x = {1}".format(i,x)) 

