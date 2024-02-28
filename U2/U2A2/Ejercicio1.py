import threading
import time
import random

def worker_thread(id, number_of_writings):
    for _ in range(number_of_writings):
        time.sleep(random.uniform(0.1, 0.3))
        print(f"I am {id}")

def exercise_1():
    pool_size = 10
    number_of_writings_range = (5, 15)

    threads = []
    for i in range(1, pool_size + 1):
        number_of_writings = random.randint(*number_of_writings_range)
        thread = threading.Thread(target=worker_thread, args=(i, number_of_writings))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    exercise_1()