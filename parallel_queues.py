from threading import Thread, Event
from queue import Queue
from time import sleep, time

event = Event()

def modify_variable(queue_in, queue_out):
    while True:
        if not queue_in.empty():
            var = queue_in.get()
            for i in range(len(var)):
                var[i] += 1
            queue_out.put(var)
        if event.is_set():
            break
    print('Stop printing')

my_var = [1, 2, 3]
queue1 = Queue()
queue2 = Queue()
queue1.put(my_var)
t = Thread(target=modify_variable, args=(queue1, queue2))
t2 = Thread(target=modify_variable, args=(queue2, queue1))
t.start()
t2.start()
t0 = time()
while time()-t0 < 5:
    try:
        sleep(1)
    except KeyboardInterrupt:
        event.set()
        break
event.set()
t.join()
t2.join()
if not queue1.empty():
    print(queue1.get())
if not queue2.empty():
    print(queue2.get())