from multiprocessing import Process
import time

def square_numbers(x):

    print(f"Square of {x} is {x * x}")
    time.sleep(3)
    
def cube_numbers(x):

    print(f"Cube of {x} is {x * x * x}")
    time.sleep(3)

if __name__ == "__main__":
    
    N = 5
    #sequential
    start = time.time()
    square_numbers(N)
    cube_numbers(N)
    print("Time take for sequential: ", time.time()-start)


    #concurrent
    start = time.time()
    t1 = Process(target = square_numbers, args = (N,))
    t2 = Process(target = cube_numbers, args = (N,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Time take for threading: ", time.time()-start)
