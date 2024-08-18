from threading import Thread, Event
from queue import Queue
from time import sleep, time

event = Event()

def modify_variable(queue_in: Queue, queue_out: Queue):
    internal_t = 0
    sleeping_t = 0
    while True:
        if not queue_in.empty():
            t0 = time()
            var = queue_in.get()
            for i in range(len(var)):
                var[i] += 1
            queue_out.put(var)
            internal_t += time()-t0
        else:
            t0 = time()
            sleep(0.001)
            sleeping_t += time()-t0
        if event.is_set():
            break
    sleep(0.1)
    print(f'Running time: {internal_t} seconds')
    print(f'Sleeping time: {sleeping_t} seconds')

my_var = [3, 4, 5]
queue1 = Queue()
queue2 = Queue()
queue1.put(my_var)
t = Thread(target=modify_variable, args=(queue1, queue1))
t2 = Thread(target=modify_variable, args=(queue1, queue1))
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