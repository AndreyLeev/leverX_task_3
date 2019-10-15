from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor

a = 0
lock = Lock()

def function(arg):
    global a
    for _ in range(arg):
        lock.acquire()
        a += 1
        lock.release()
        

def main():
    workers = 5
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for _ in range(workers):
            executor.submit(function, 1000000)

    print("----------------------", a)  # ???


main()
