import threading
import random
import math

def mean_thread(data):
    mean_value = sum(data) / len(data)
    print(f"Mean: {mean_value}")

def min_max_thread(data):
    min_value = min(data)
    max_value = max(data)
    print(f"Min: {min_value}, Max: {max_value}")

def std_dev_thread(data):
    mean_value = sum(data) / len(data)
    variance = sum((x - mean_value) ** 2 for x in data) / len(data)
    std_dev_value = math.sqrt(variance)
    print(f"Standard Deviation: {std_dev_value}")

def exercise_2():
    pool_size = 3
    data = [random.randint(1, 100) for _ in range(100)]

    threads = [
        threading.Thread(target=mean_thread, args=(data,)),
        threading.Thread(target=min_max_thread, args=(data,)),
        threading.Thread(target=std_dev_thread, args=(data,))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    exercise_2()
